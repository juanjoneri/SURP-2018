import itertools
from .card import Card
from .deck import Deck
from .lookup import LookupTable

class Evaluator(object):
    """
    Evaluates hand strengths using a variant of Cactus Kev's algorithm:
    http://suffe.cool/poker/evaluator.html

    I make considerable optimizations in terms of speed and memory usage, 
    in fact the lookup table generation can be done in under a second and 
    consequent evaluations are very fast. Won't beat C, but very fast as 
    all calculations are done with bit arithmetic and table lookups. 
    """

    def __init__(self):

        self.table = LookupTable()
        
        self.hand_size_map = {
            2 : self._two_three_or_four,
            3 : self._two_three_or_four,
            4 : self._two_three_or_four,
            5 : self._five,
            6 : self._six,
            7 : self._seven
        }

    def evaluate(self, cards, board=[]):
        """
        This is the function that the user calls to get a hand rank. 

        Supports empty board, etc very flexible. No input validation 
        because that's cycles!
        """
        all_cards = cards + board
        return self.hand_size_map[len(all_cards)](all_cards)

    def _two_three_or_four(self, cards):
        """
        Performs five_card_eval() on a set of cards that contains less than 5 cards,
        plus the worst possible other cards you could pair them with so that 
        we get a hand of 5 but no new games are formed.
        """
        used_suits = {Card.get_suit_int(card) for card in cards}
        used_ranks = {Card.get_rank_int(card) for card in cards}
        
        available_suits = set(Card.INT_SUITS) - used_suits
        available_ranks = set(Card.INT_RANKS) - used_ranks

        worst_complement = []
        # because this suit has not been used, we can add 3 cards of that suit
        # without generating a flush:
        if any(available_suits):
            random_suit = available_suits.pop()
        else:
            # 4 cards already in hand with dif suits, any suit will do
            random_suit = used_suits.pop()
        for rank in sorted(available_ranks)[:5-len(cards)]:
            worst_complement.append(Card.new_from_int(rank, random_suit))

        # check if we generated a straight, if we have, swap biggest card for the next smallest
        evaluation = self._five(cards + worst_complement)
        if self.get_rank_class(evaluation) == 5:
            next_available_rank = sorted(available_ranks)[5-len(cards)]
            worst_complement[-1] = Card.new_from_int(next_available_rank, random_suit)
            evaluation = self._five(cards + worst_complement)
        
        return evaluation
        
    def _five(self, cards):
        """
        Performs an evalution given cards in integer form, mapping them to
        a rank in the range [1, 7462], with lower ranks being more powerful.

        Variant of Cactus Kev's 5 card evaluator, though I saved a lot of memory
        space using a hash table and condensing some of the calculations. 
        """
        # if flush
        if cards[0] & cards[1] & cards[2] & cards[3] & cards[4] & 0xF000:
            handOR = (cards[0] | cards[1] | cards[2] | cards[3] | cards[4]) >> 16
            prime = Card.prime_product_from_rankbits(handOR)
            return self.table.flush_lookup[prime]

        # otherwise
        else:
            prime = Card.prime_product_from_hand(cards)
            return self.table.unsuited_lookup[prime]

    def _six(self, cards):
        """
        Performs five_card_eval() on all (6 choose 5) = 6 subsets
        of 5 cards in the set of 6 to determine the best ranking, 
        and returns this ranking.
        """
        minimum = LookupTable.MAX_HIGH_CARD

        all5cardcombobs = itertools.combinations(cards, 5)
        for combo in all5cardcombobs:

            score = self._five(combo)
            if score < minimum:
                minimum = score

        return minimum

    def _seven(self, cards):
        """
        Performs five_card_eval() on all (7 choose 5) = 21 subsets
        of 5 cards in the set of 7 to determine the best ranking, 
        and returns this ranking.
        """
        minimum = LookupTable.MAX_HIGH_CARD

        all5cardcombobs = itertools.combinations(cards, 5)
        for combo in all5cardcombobs:
            
            score = self._five(combo)
            if score < minimum:
                minimum = score

        return minimum

    def get_rank_class(self, hr):
        """
        Returns the class of hand given the hand hand_rank
        returned from evaluate. 
        """
        if hr >= 0 and hr <= LookupTable.MAX_STRAIGHT_FLUSH:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_STRAIGHT_FLUSH]
        elif hr <= LookupTable.MAX_FOUR_OF_A_KIND:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_FOUR_OF_A_KIND]
        elif hr <= LookupTable.MAX_FULL_HOUSE:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_FULL_HOUSE]
        elif hr <= LookupTable.MAX_FLUSH:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_FLUSH]
        elif hr <= LookupTable.MAX_STRAIGHT:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_STRAIGHT]
        elif hr <= LookupTable.MAX_THREE_OF_A_KIND:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_THREE_OF_A_KIND]
        elif hr <= LookupTable.MAX_TWO_PAIR:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_TWO_PAIR]
        elif hr <= LookupTable.MAX_PAIR:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_PAIR]
        elif hr <= LookupTable.MAX_HIGH_CARD:
            return LookupTable.MAX_TO_RANK_CLASS[LookupTable.MAX_HIGH_CARD]
        else:
            raise Exception("Inavlid hand rank, cannot return rank class")

    def class_to_string(self, class_int):
        """
        Converts the integer class hand score into a human-readable string.
        """
        return LookupTable.RANK_CLASS_TO_STRING[class_int]

    def get_five_card_rank_percentage(self, hand_rank):
        """
        Scales the hand rank score to the [0.0, 1.0] range.
        """
        return float(hand_rank) / float(LookupTable.MAX_HIGH_CARD)

    def hand_summary(self, board, hands):
        """
        Gives a sumamry of the hand with ranks as time proceeds. 

        Requires that the board is in chronological order for the 
        analysis to make sense.
        """

        assert len(board) == 5, "Invalid board length"
        for hand in hands:
            assert len(hand) == 2, "Inavlid hand length"

        line_length = 10
        stages = ["PRE-FLOP", "FLOP", "TURN", "RIVER"]

        for i in range(len(stages)):
            line = ("=" * line_length) + " {} " + ("=" * line_length) 
            print(line.format(stages[i]))
            
            best_rank = 7463  # rank one worse than worst hand
            winners = []
            for player, hand in enumerate(hands):

                # evaluate current board position
                rank = self.evaluate(hand) if i == 0 else self.evaluate(hand, board[:(i + 2)])

                rank_class = self.get_rank_class(rank)
                class_string = self.class_to_string(rank_class)
                percentage = 1.0 - self.get_five_card_rank_percentage(rank)  # higher better here
                print("Player {} hand = {}, percentage rank among all hands = {}".format(
                    player + 1, class_string, percentage))

                # detect winner
                if rank == best_rank:
                    winners.append(player)
                    best_rank = rank
                elif rank < best_rank:
                    winners = [player]
                    best_rank = rank

            # if we're not on the river
            if i != stages.index("RIVER"):
                if len(winners) == 1:
                    print("Player {} hand is currently winning.\n".format(winners[0] + 1,))
                else:
                    print("Players {} are tied for the lead.\n".format([x + 1 for x in winners]))

            # otherwise on all other streets
            else:
                print()
                print(("=" * line_length) + " HAND OVER " + ("=" * line_length)) 
                if len(winners) == 1:
                    print("Player {} is the winner with a {}\n".format(winners[0] + 1, 
                        self.class_to_string(self.get_rank_class(self.evaluate(hands[winners[0]], board)))))
                else:
                    print("Players {} tied for the win with a {}\n".format(winners, 
                        self.class_to_string(self.get_rank_class(self.evaluate(hands[winners[0]], board)))))




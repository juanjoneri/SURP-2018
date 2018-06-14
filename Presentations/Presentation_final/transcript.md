## Deep Learning + Causal Inference
Last time I spoke about how there are two fonteeres in Artificial Intelligence
The two of which solve very different tasks.

To remind you, I shared how deep learning has been really successful in the last few years,
due to its power to extract meaning from high dimensional data like images or audio.
Causal inference, is still the best candidate for modeling uncertain domains, and can help
us equip an agent with the ability of making choices under uncertainty.

So we wanted to combine the two approaches to solve a task that is more general that either.
Candidates included movie reccomendation, and medical research.

## Building a Poker Bot

Poker has been really popular among reseaerchers of causal inference because it has lots of
uncertainty and it is crusial to quantify this uncertainty in order to make decisions.

We thought that apart from uderstanding the state of a game, a poker agent could potentially
benefit from the advancements in deep learning, for tasks like understanding the opponent's
reaction and assessing an underlying level of confidence that it might imply

## The Task

This image represents the ML layer of the poker bot, which is in charge of understanding
what is going on.

So that is what we did. On the left we have a poker game from the perspective of the poker bot.
poker bot is a web app that interfaces with the world in three ways:

  - picture of the cards it is holding
  - picture from the opp face
  - recordings of the opp actions

The client performs some preprocessing of this data: for example we compress the images. We
the upload this data to the cloud, where we have multiple microservices in charge of the
specific tasks of analyzing confidence, transcribing the audio, and understanding the cards.

## The DAG

This graph represents the second component of our poker bot, the Bayesian Netork.
This network encodes how the system works for the agent. So for example this network
encodes the fact that the size of the pot directly influences my opponents actions somehow.

There are 3 different kinds of nodes that make up the graph:
  - Yellow: Deep Learning Nodes
  - Red: Simulated Nodes
  - Blue: Learned Nodes

Training this network has been the hardest challenge for me in this project.

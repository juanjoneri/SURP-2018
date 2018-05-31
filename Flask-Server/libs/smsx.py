import nexmo
import json

def send_sms_to(message, number):
    with open('../../nexmokey.json') as f:
        credentials = json.load(f)
        client = nexmo.Client(**credentials)
        client.send_message({
            'from': 12013801966,
            'to': number,
            'text': message,
        })

def main():
    send_sms_to('Someone is using you website!', 12132745685)

if __name__ == '__main__':
    main()
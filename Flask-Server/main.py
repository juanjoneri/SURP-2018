import logging
from flask import Flask, request
from libs.visionx import detect_labels_uri, detect_joy
from libs.smsx import send_sms_to

app = Flask(__name__)

@app.route('/')
def homepage():
    send_sms_to('Someone is in poker-bot-v1\'s home page')
    return app.send_static_file('index.html')

@app.route('/facial-expression')
def facial_expression():
    image_url = request.args.get('image_url')
    joy_list = detect_joy(image_url)

    return \
    '''
    <h1>The image at {}</h1>
    <h2>displays the following visual queues from 1 to 5:</h2>
    <p>{}</p>
    '''.format(image_url, joy_list)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)

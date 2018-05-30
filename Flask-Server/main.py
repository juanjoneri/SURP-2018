import logging
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return app.send_static_file('index.html')

@app.route('/facial-expression')
def facial_expression():
    #labels = visionx.detect_labels_uri('https://www.pokersites.ca/images/top-players/daniel-negreanu-sm.jpg')
    image_url = request.args.get('image_url')
    return \
    '''
    <h1>The image at {}</h1>
    <h2>has the following tags:</h2>
    <p>{}</p>
    '''.format(image_url, 'some label')

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)

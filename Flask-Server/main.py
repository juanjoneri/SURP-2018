import logging
from ../Facial-Expression/visionx.py import detect_labels_uri

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    labels = detect_labels_uri('https://www.pokersites.ca/images/top-players/daniel-negreanu-sm.jpg')
    return f'{labels[0].description}'


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)

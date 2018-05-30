import logging
from flask import Flask, request
from libs.visionx import detect_labels_uri

app = Flask(__name__)

@app.route('/')
def homepage():
    return app.send_static_file('index.html')

@app.route('/facial-expression')
def facial_expression():
    image_url = request.args.get('image_url')
    labels = detect_labels_uri(image_url)

    return \
    '''
    <h1>The image at {}</h1>
    <h2>has the following tags:</h2>
    <p>{}</p>
    '''.format(image_url, list(map(lambda label: (label.description, label.score), labels)))

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)

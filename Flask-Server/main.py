import logging
from flask import Flask, request, jsonify, redirect, url_for, render_template
from libs.visionx import detect_labels_uri, detect_joy
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'flac', 'wav'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

DATA_FILES = ['cards_image', 'reaction_image', 'action_sound']

@app.route('/', methods=['GET', 'POST'])
def homepage():
    uploaded_data = dict()
    if request.method == 'POST':
        for data_file in DATA_FILES:
            if data_file not in request.files:
                continue
            
            file = request.files[data_file]
            filename = file.name
            if file.filename == '':
                continue
            
            extension = file.filename.rsplit('.', 1)[1].lower()
            if extension in ALLOWED_EXTENSIONS:
                filename = secure_filename(file.filename)
                uploaded_data[data_file] = filename
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)

    return render_template('index.html', **uploaded_data)


@app.route('/instructions')
def instruction():
    return app.send_static_file('instructions.html')

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

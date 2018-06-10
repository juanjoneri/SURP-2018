import logging
import operator
import os
from flask import Flask, request, jsonify, redirect, url_for, render_template

from libs.visionx import detect_labels_uri, detect_joy
from libs.storagex import upload_file_name
from libs.imagex import save_small
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'flac', 'wav'])
IMG_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

DATA_FILES = ['cards_image', 'reaction_image', 'action_audio']

uploaded_data = dict()

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        for data_file in DATA_FILES:
            if data_file not in request.files:
                continue

            # RETREIVE METADATA OF FILE TO BE UPLOADED
            file = request.files[data_file]
            filename = file.filename
            extension = filename.rsplit('.', 1).pop().lower()

            if filename == '':
                continue

            if extension in IMG_EXTENSIONS:
                # STORE A SMALL VERSION OF THE PICTURE MOMENTARILY
                temp_dst = os.path.join(
                    app.config['UPLOAD_FOLDER'], 'temp-'+file.filename)
                save_small(file, 100, 400, temp_dst)

            if extension in ALLOWED_EXTENSIONS:
                folder = data_file
                file_uri = upload_file_name(temp_dst, '{}/{}'.format(folder, filename), file.content_type)
                uploaded_data[data_file] = file_uri
                if data_file == 'reaction_image':
                    reaction = detect_joy(file_uri)
                    uploaded_data['reaction'] = max(reaction.items(), key=operator.itemgetter(1))[0]

            # REMOVE TEMP SMALL IMAGE FORM STORAGE
            file.close()
            os.remove(temp_dst)

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

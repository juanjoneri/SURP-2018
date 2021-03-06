import logging
import operator
import os
from flask import Flask, request, jsonify, redirect, url_for, render_template

from libs.visionx import detect_labels_uri, detect_joy
from libs.storagex import upload_file_name, upload_file
from libs.imagex import save_small
from libs.speechx import detect_speech_uri
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'flac', 'wav'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
DATA_FILES = ['cards_image', 'reaction_image', 'action_audio']

uploaded_data = {
    'cards_image': 'static/Card-Placeholder.png',
    'reaction_image': 'static/Reaction-Placeholder.png',
    'action': 'Upload a recording of what OPP Said!',
    'reaction': 'Take a picture of my opponent!'}

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        # ITERATE OVER ALL DATA WE ASK FROM THE USER
        for data_file in DATA_FILES:

            if data_file not in request.files:
                continue

            # RETREIVE METADATA OF FILE TO BE UPLOADED
            file = request.files[data_file]
            filename = file.filename
            extension = filename.rsplit('.', 1).pop().lower()

            if extension in ALLOWED_EXTENSIONS:

                folder = data_file # foler name in bucket

                if data_file in ['reaction_image', 'cards_image']:
                    # STORE A SMALL VERSION OF THE PICTURE MOMENTARILY
                    temp_dst = os.path.join(
                        app.config['UPLOAD_FOLDER'], 'temp-'+file.filename)
                    save_small(file, 256, 256, temp_dst)

                    # UPLOAD COMPRESSED IMAGE TO BUCKET
                    file_uri = upload_file_name(
                        temp_dst, '{}/{}'.format(folder, filename), file.content_type)

                    # REMOVE COMPRESSED IMG FROM SERVER
                    os.remove(temp_dst)

                    # GET THE ANALYSIS OF THE REACTION FROM GC-AI
                    if data_file == 'reaction_image':
                        reaction = detect_joy(file_uri)
                        if reaction:
                            uploaded_data['reaction'] = 'I see {} in my opponent\'s face...'.format(max(
                                reaction.items(), key=operator.itemgetter(1))[0])
                        else:
                            uploaded_data['reaction'] = 'I can\'t see my opponent\'s face!'

                elif data_file in ['action_audio']:
                    # UPLOAD AUDIO TO BUCKET
                    file_uri = upload_file(
                        file.read(), '{}/{}'.format(folder, filename), file.content_type)

                    reaction = detect_speech_uri('gs://poker-bot-src-bucket/action_audio/{}'.format(filename))
                    uploaded_data['action'] = reaction['transcript']


                # SAVE TO TEMPLATE METADATA
                uploaded_data[data_file] = file_uri

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
    #app.run(host='0.0.0.0', port=8080, debug=True)

# Setting up the App

## Server
```
cd Flask-Server/
pip3 install -r requirements.txt
gcloud app deploy
```
https://poker-bot-v1.appspot.com/

## Local Machine
```
cd Flask-Server/
pip3 install -r requirements.txt
export FLASK_APP=main.py
flask run
```
http://127.0.0.1:5000/

# Setting up GCloud API credentials
1. Find where apikey.json is located in `<path>`
2. Add the following at the end of ~/.profile
```
export GOOGLE_APPLICATION_CREDENTIALS=<path>
```

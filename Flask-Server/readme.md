# How to use Google App Engine

## Test
```
cd Flask-Server/
pip3 install -r requirements.txt
export FLASK_APP=main.py
flask run
```
http://127.0.0.1:5000/

## Deploy

```
export GOOGLE_APPLICATION_CREDENTIALS=<path>
sudo gcloud init
sudo gcloud app deploy
```
https://poker-bot-v1.appspot.com/

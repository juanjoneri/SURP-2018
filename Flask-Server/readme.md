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

> No quotation marks go around the path
```
export GOOGLE_APPLICATION_CREDENTIALS=<path>
sudo gcloud init
sudo gcloud app deploy
```
https://poker-bot-v1.appspot.com/

## Others

Set public bucket by default when user uploads

```
sudo gsutil defacl set public-read gs://poker-bot-src-bucket
```


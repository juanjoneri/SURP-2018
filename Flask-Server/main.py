import logging

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hi Juan'


def main():
    app.run(host='127.0.0.1', port=8080, debug=True)

if __name__ == '__main__':
    main()
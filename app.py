from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is home!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
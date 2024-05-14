#!/usr/bin/python3
""" A script that starts a flask web app """

from flask import Flask
app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def start():
    # Function for the index call
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(port=5000)

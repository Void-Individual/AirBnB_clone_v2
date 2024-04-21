#!/usr/bin/python3
"""A script that starts a flask app with new routes
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start():
    # Function to display the index page
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    # Function to display the hbnb page
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True)

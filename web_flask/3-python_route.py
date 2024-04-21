#!/usr/bin/python3
# Let the python app display an additional function

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

@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    # Function to display a page after /c
    return  f"C {text}"

@app.route('/python/', strict_slashes=False)
def python_default():
    return "Python is cool"

@app.route('/python/<text>', strict_slashes=False)
def python_text(text=None):
    # Function to display a page after /python
        return f"Python {text}"

if __name__ == '__main__':
    app.run(debug=True)

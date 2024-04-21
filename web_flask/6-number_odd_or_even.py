#!/usr/bin/python3
# Let the python app display an additional function

from flask import Flask, render_template
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
def python_text(text):
    # Function to display a page after /python
        return f"Python {text}"

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    # Function to display a page after a /number
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    # Function to display an html page
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    # Function to display a different page depending on odd/even
    if (int(n) % 2 == 0):
        return render_template('6-number_odd_or_even.html', n=n,
                               value="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n,
                               value="odd")


if __name__ == '__main__':
    app.run(debug=True)

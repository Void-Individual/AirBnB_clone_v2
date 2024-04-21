#!/usr/bin/python3
"""Script to start flask and run states
"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_the_db(exception=None):
    # Function to clear previous session
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    # Function to display html page full of states
    from models.state import State
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(debug=True)

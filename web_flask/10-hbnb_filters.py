#!/usr/bin/python3
'''a script that starts a Flask web application has routes for
hbnb airBnB clone
'''

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    '''Tear down seesion: db'''
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    '''Print for each state: id & name'''
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

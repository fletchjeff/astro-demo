import flask
from flask import request, jsonify
import random
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

randomlist = random.sample(range(1, 30), random.randint(1,10))

@app.route('/', methods=['GET'])
def home():
    return '''API Tester'''


# A route to return all of the available entries in our catalog.
@app.route('/api', methods=['GET'])
def api_all():
    print(datetime.datetime.now())
    return jsonify(randomlist)

app.run(host='0.0.0.0')
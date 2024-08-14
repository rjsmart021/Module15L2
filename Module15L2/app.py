from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError

# local import for db_connection
from connect_db import connect_db, Error

app = Flask(__name__)
app.json.sort_keys = False # maintain order set in program
ma = Marshmallow(app)

# homepage
@app.route('/')
def home():
    return "<h1>Welcome to the Fitness Scheduler!</h1>\
<h2>Let's get yoked!</h2><br>\
<img src=\"https://as1.ftcdn.net/v2/jpg/05/53/59/18/1000_F_553591884_dkgQVT2nF94pyW1PkD6rzx5hzIWtt256.jpg\" >"

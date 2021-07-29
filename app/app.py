from flask import Flask
from flask_app import flask_app

app = Flask(__name__)
app.register_blueprint(flask_app)
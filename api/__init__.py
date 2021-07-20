import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer

ERROR="error"
OK="ok"


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET"] = os.environ.get("SECRET")
db = SQLAlchemy(app)
blob = Blobber(analyzer=NaiveBayesAnalyzer())

from api import routes
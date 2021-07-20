from api import db


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    messages = db.relationship("Message", lazy="dynamic")

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    sender = db.Column(db.Integer, db.ForeignKey("user.uid"), nullable=False)
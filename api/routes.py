from api import app, blob, ERROR, OK, db
from api.model import User, Message
from api.utils import generate_response

from flask import jsonify, request

@app.route("/")
def index():
    return "GET STARTED USING NLP APIs", 200

@app.route("/predict-sentiment", methods=["POST"])
def predict_sentiment():
    try:
        text = str(request.get_json()["text"])
        predict = blob(text).sentiment
        response = {
            "happy": predict.p_pos,
            "angry": predict.p_neg,
            "status": OK
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify(status=ERROR, message=str(e)), 400


@app.route("/register", methods=["POST"])
def register_user():
    try:
        username = str(request.get_json()["username"])
        user = User(name=username)
        db.session.add(user)
        db.session.commit()
        response = {
            "uid": user.uid
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify(status=ERROR, message=str(e)), 400

@app.route("/generate-response", methods=["POST"])
def get_response():
    try:
        msg = request.get_json()["message"]
        uid = request.get_json()["uid"]
        user = User.query.get(uid)
        if user is None:
            return jsonify(status=ERROR, message=f"No user found with {uid} id"), 400
        messages = list(map(lambda msg: msg.message, user.messages))
        print(messages)
        output = generate_response(messages, msg)
        new_message = Message(message=msg, sender=uid)
        db.session.add(new_message)
        db.session.commit()
        response = {
            "response" : output,
            "status": OK
        }
        return jsonify(response), 200
    except Exception as e:
        print(e)
        return jsonify(status=ERROR, message=str(e)), 400
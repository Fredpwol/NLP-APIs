from flask import Flask, request, jsonify
from utils import generate_response


from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Blobber

blob = Blobber(analyzer=NaiveBayesAnalyzer())
ERROR = "ERROR"
OK = "OK"
app = Flask(__name__)
users = dict() #this is used as a minimal database for storing users and their conversations.

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


@app.route("/auto-response")
def get_response():
    try:
        msg = request.get_json()["message"]
        uid = request.get_json()["uid"]
        history, output = generate_response(users.get(uid, None), msg)
        response = {
            "response" : output,
            "status": OK
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify(status=ERROR, message=str(e)), 400

if __name__ == "__main__":
    app.run(debug=True)
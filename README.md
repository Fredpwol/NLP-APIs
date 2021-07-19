# NLP APIs

Get sentiment and get message response based on chat history.
The sentiment analyses uses text blob and the NaiveBayesAnalyzer model while the response generator uses microsoft DialoGPT model.


## Getting Started

Make sure you have python installed on your machine. Install dependecies using 
```
pip install -r requirements.txt
```

Start the Flask server using 
```
python app.py
```

# Endpoints

<b>`/predict-sentiment`</b>
This is used for giving a sentiment score of a text string. this endpoint recieves POST requests with a JSON payload structured like this for example
```json
{
"text": "We had a lovely holiday at our gradma's house"
}
```
The response will be a json http response like this
```json
{
    "angry": 0.34464859056826985,
    "happy": 0.655351409431729
}
```
Where angry is a probability the message had an angry or bad sentiment, and happy means a positive or good sentiment.

<b>`/generate-response`</b>
For getting automatic response from a user based on the conversation history, it takes in POST request with a JSON payload containing user id and a message like this.
```json
{
    "uid": 0,
    "message": "What do you do for a living?"
}
```
The response will be a json http response like this
```json
{
    "response": "I'm a software engineer.",
    "status": "OK"
}
```
The response is a reply to the message sent to the endpoint by the user.
## Note

You can change the model type for the DialoGPT model to any size depending on what you want. the small model is very fast but isn't good at generating good response.


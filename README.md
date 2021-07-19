# NLP stuffs

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

## Note

You can change the model type for the DialoGPT model to any size depending on what you want. the small model is very fast but isn't good at generating good response.


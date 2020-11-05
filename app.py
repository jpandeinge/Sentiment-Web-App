import pickle
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


model = pickle.load(open('model_pipeline.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():


    if request.method == 'POST':
        message = request.form['message']
        prediction = model.predict([message])


    return render_template('index.html', prediction_text='The text sentiment is {}'.format(prediction))

@app.route('/results', methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([list(data.values())])

    output = prediction[0]
    return jsonify(ouput)

if __name__ == "__main__":
    app.run(debug=True)
    
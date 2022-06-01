import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

application = Flask(__name__) #Initialize the flask App
model = pickle.load(open('LightGBM_model.xml', 'rb'))

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    # output = round(prediction[0], 2)
    # return render_template('index.html', prediction_text='This Transaction is {}'.format(prediction))
    if prediction == 1:
        return render_template('index.html', prediction_text='This Transaction is Fraudulent')
    if prediction == 0:
        return render_template('index.html', prediction_text='This Transaction is Normal')

if __name__ == "__main__":
    application.run(debug=True)

from flask import Flask, request
import requests
import pickle

model = pickle.load(open('model_api/model_decisiontree_0801.pkl', 'rb'))
app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
    """
    Get prediction based on hospital record and flag riskiness
    
    MVP: return yes or no for readmitted in less than 30 days
    Post-MVP: return risk score (0-1000) where > 800 is high risk and >= 900 is very high risk
    """
    # get user data
    data = request.get_json()

    # setup data for model
    # user_inputs = [data[], data[]]
    
    prediction = model.predict([user_inputs])[0]

    prediction_mapping = {0: 'Patient Has CKD', 1:'Patient Does Not Have CKD'}
    
    return prediction_mapping[prediction]
#from sklearn.linear_model import LinearRegression
import pickle
import numpy as np
import sklearn
import tensorflow as tf
from keras.models import Sequential
#from tensorflow.keras.models import Sequential
import random
#from tensorflow import keras 

filenames = {
    "models" : {
        "electrique" : "./dumps/electrique_model.sav",
        "essence" : "./dumps/essence_model.sav",
        "auto-portee" : "./dumps/autoportee_model.sav",
    },
    "scalers" : {
        "electrique" : "./dumps/electrique_scaler.sav",
        "essence" : "./dumps/essence_scaler.sav",
        "auto-portee" : "./dumps/autoportee_scaler.sav",
    }
}

def create_features(mower):
    margin_prop = mower['margin'] / mower['price']
    failure_price = mower['price'] / mower['failure_rate']
    capacity_price = mower['capacity'] / mower['price']
    quality_Hight = 1 if mower['quality'] == 'Low' else 0
    quality_Medium = 1 if mower['quality'] == 'Medium' else 0
    quality_Low = 1 if mower['quality'] == 'Hight' else 0
    return np.array([[    
        mower['capacity'],
        mower['failure_rate'],
        mower['margin'],
        mower['price'],
        mower['prod_cost'],
        margin_prop, 
        failure_price,
        capacity_price ,
        quality_Hight, 
        quality_Medium, 
        quality_Low
        ]])

def scale(mower,product_type):
    loaded_scaler = pickle.load(open(filenames["scalers"][product_type], 'rb'))
    mower_scaled = loaded_scaler.transform(mower)
    return mower_scaled

def load_model(product_type):
    loaded_model = pickle.load(open(filenames["models"][product_type], 'rb'))
    return loaded_model

def predict_attractiveness(mower):
    product_type = mower['product_type']
    features = create_features(mower)
    features_scaled = scale(features,product_type)
    loaded_model = load_model(product_type)
    return loaded_model.predict(features_scaled)
        

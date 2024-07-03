#data validation layer 
import joblib
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import os 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

#model=joblib.load('model.pkl')
#tfidf = joblib.load('tfidf.pkl')

location = 'C:/Users/ddebbiche/Desktop/NLP/spam_ham'
fullpath = os.path.join(location, 'model_nlp.pkl')
model = joblib.load(fullpath)

location = 'C:/Users/ddebbiche/Desktop/NLP/spam_ham'
fullpath = os.path.join(location, 'tfidf_nlp.pkl')
tfidf = joblib.load(fullpath)

class Message(BaseModel):
    text : str
class Prediction(BaseModel):
    prediction : int 
    
app=FastAPI() 
   
#define route spam or ham
@app.post("/predict", response_model= Prediction)

async def predict(message : Message):
    input_data = tfidf.transform([message.text]).toarray()
    prediction = model.predict(input_data)[0]
    #print('le type de prediction est',type(int(prediction)))
    return Prediction(prediction=int(prediction))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

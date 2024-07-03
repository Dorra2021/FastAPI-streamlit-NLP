import streamlit as st 
import json
import requests


# Définir l'URL de l'API
API_URL = "http://127.0.0.1:8000/predict"


st.title("Spam or no-Spam App")

#input of the user
input_text=st.text_area("Enter the message")
if st.button('Predict'):
    # Make the API call
    data = {"text": input_text}
    response=requests.post(API_URL,json=data)
    
    if response.status_code == 200:
            # Extraire la prédiction de la réponse JSON
            prediction = response.json().get("prediction")
            
            # Afficher le résultat
            if prediction == 1:
                st.header("Spam")
            else:
                st.header("Not Spam")
    else:
            st.header("Erreur : La requête à l'API a échoué.")
else:
        st.header("Veuillez entrer un message.")
        
   # if response==1:
    #    st.header("Spam")
    #elif response==0:
    #    st.header("Not Spam")
    
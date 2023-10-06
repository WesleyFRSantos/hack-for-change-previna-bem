from flask import Flask, request, jsonify

from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
import os
import numpy as np

modelo = pickle.load(open('./models/modelo.sav','rb'))
modelo_ha = pickle.load(open('./models/model_ha.pkl','rb'))


app = Flask(__name__)

@app.route('/')
def home():
    return "API rodando"

# 127.0.0.1:5000/predict_diabetes/?gender=Male&age=55&heart_disease=1&smoking_history=current&bmi=25.5&HbA1c_level=6.6&blood_glucose_level=140&hypertension=1

@app.route('/predict_diabetes/')
def cotacao():

    # Esses parâmetros serão enviados do front-end através da URL da requisição
    # Adaptar para cada modelo

    gender = request.args.get('gender', type = str)
    age = request.args.get('age', type = int)
    hypertension = request.args.get('hypertension', type = int)
    heart_disease = request.args.get('heart_disease', type = int)
    smoking_history = request.args.get('smoking_history', type = str)
    bmi = request.args.get('bmi', type = float)
    HbA1c_level = request.args.get('HbA1c_level', type = float)
    blood_glucose_level = request.args.get('blood_glucose_level', type = float)

    # O meu modelo é uma pipeline e eu peciso passar os dados brutos e com as colunas, por isso crio um dataframe de 1 linha com os dados de input
    # cada parâmetro desse está presente na parte final da URL ... gender=male&age=21 ... 
    
    input_values = {
        'gender':[gender],
        'age':[age],
        'hypertension':[hypertension],
        'heart_disease':[heart_disease],
        'smoking_history':[smoking_history],
        'bmi':[bmi],
        'HbA1c_level':[HbA1c_level],
        'blood_glucose_level':[blood_glucose_level]
    }
    input_modelo = pd.DataFrame.from_dict(input_values)

    # print(input_modelo)
    probabilidade_doenca = modelo.predict_proba(input_modelo)
    # print('Proba: ',preco[0][0])
    return jsonify(probabilidade_diabetes=probabilidade_doenca[0][0])

# 127.0.0.1:5000/predict_heart_attack/?age=1&sex=1&cp=1&trtbps=1&chol=1&fbs=1&restecg=1&thalachh=1&exng=1&oldpeak=1.2&slp=1&caa=1&thall=1

@app.route('/predict_heart_attack/')
def cotacao_heart_attack():

    # Esses parâmetros serão enviados do front-end através da URL da requisição
    # Adaptar para cada modelo
    
    age = request.args.get('age', type = int)
    sex = request.args.get('sex', type = int)
    cp = request.args.get('cp', type = int)
    trtbps = request.args.get('trtbps', type = int)
    chol = request.args.get('chol', type = int)
    fbs = request.args.get('fbs', type = int)
    restecg = request.args.get('restecg', type = int)
    thalachh = request.args.get('thalachh', type = int)
    exng = request.args.get('exng', type = int)
    oldpeak = request.args.get('oldpeak', type = float)
    slp = request.args.get('slp', type = int)
    caa = request.args.get('caa', type = int)
    thall = request.args.get('thall', type = int)

    input_values_ha = {
        'age':[age],
        'sex':[sex],
        'cp':[cp],
        'trtbps':[trtbps],
        'chol':[chol],
        'fbs':[fbs],
        'restecg':[restecg],
        'thalachh':[thalachh],
        'exng':[exng],
        'oldpeak':[oldpeak],
        'slp':[slp],
        'caa':[caa],
        'thall':[thall]
    }

    input_modelo_ha = pd.DataFrame.from_dict(input_values_ha)

    probabilidade_doenca_ha = modelo_ha.predict_proba(input_modelo_ha)
    # print('Proba: ',preco[0][0])
    return jsonify(probabilidade_heart_attack=probabilidade_doenca_ha[0][0])


app.run(debug=True, host='0.0.0.0')
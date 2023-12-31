from flask import Flask,redirect,request,render_template
import numpy as np
import pandas as pd
import sys
from src.exception import CustomException
from src.logger import logging

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__)

app= application

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/predictdata',methods =['GET','POST'])
def predict_datapoint():
    
    if request.method =='GET':
        return render_template('home.html')

    else:
        
        data= CustomData( gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
            )
        logging.info(data)
        pred_df = data.get_data_as_dataframe()
        logging.info(pred_df)
        print(pred_df)
        print("data before prediction")
        
        
        predict_pipeline = PredictPipeline()
        pred_score =predict_pipeline.predict(pred_df)
        print(f"After prediction:-{pred_score}")
        return render_template('home.html',results=pred_score[0])
    

if __name__ == "__main__":
    
    app.run(host= "0.0.0.0",port=8080)
            

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from joblib import load
from sqlalchemy import insert
import pandas as pd
from ..models.predictions import Prediction
from .. import db
from ..forms.predictionForm import PredictionForm

prediction = Blueprint('prediction', __name__)

@prediction.route('/predict')
@login_required
def predict():
    
    form = PredictionForm()
    return render_template('predictionForm.html', name=current_user.name, form=form)

@prediction.route('/result', methods=['POST'])
@login_required
def result():
    
    form = PredictionForm()
    eNet = load('app/estimators/elasticnet.joblib')
    data = {}
    
    if request.form:
        for var in ['overallInteriorQuality', 'totalSf', 'garageArea', 
                    'fireplaces','roomNbAbvGrd','overallExteriorQuality', 
                    'fullLot', 'timeBetweenSale', 'saleYear', 'neighborhood']:
            if var in ['neighborhood']:
                data[var] = request.form[var]
            else:
                data[var] = int(request.form[var])

        price = eNet.predict(pd.DataFrame(data, index=[0]))
    
        pred = Prediction(
            user_id = current_user.id,
            overallInteriorQuality = request.form.get("overallInteriorQuality"),
            totalSf = request.form.get("totalSf"),
            garageArea = request.form.get("garageArea"),
            fireplaces = request.form.get("fireplaces"),
            roomNbAbvGrd = request.form.get("roomNbAbvGrd"),
            overallExteriorQuality = request.form.get("overallExteriorQuality"),
            fullLot = request.form.get("fullLot"),
            timeBetweenSale = request.form.get("timeBetweenSale"),
            saleYear = request.form.get("saleYear"),
            neighborhood = request.form.get("neighborhood"),
            result = int(price)
        )
        
        db.session.add(pred)
        db.session.commit()
        
    return render_template('predictionForm.html', name=current_user.name, data=int(price), form=form)
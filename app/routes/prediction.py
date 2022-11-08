from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from joblib import load
import pandas as pd
from ..models.users import User
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
    for var in ['overallInteriorQuality', 'totalSf', 'garageArea', 
                'fireplaces','roomNbAbvGrd','overallExteriorQuality', 
                'fullLot', 'timeBetweenSale', 'saleYear', 'neighborhood']:
        if var in ['neighborhood']:
            data[var] = request.form[var]
        else:
            data[var] = int(request.form[var])

    pred = eNet.predict(pd.DataFrame(data, index=[0]))
    return render_template('predictionForm.html', name=current_user.name, data=int(pred), form=form)
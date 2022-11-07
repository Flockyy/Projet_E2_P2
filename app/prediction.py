from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from .models.users import User
from . import db

prediction = Blueprint('prediction', __name__)

@prediction.route('/prediction')
@login_required
def predict():
    return render_template('predictionForm.html')

@prediction.route('/result')
@login_required
def predict():
    return render_template('result.html')




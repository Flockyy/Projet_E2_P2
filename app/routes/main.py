from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.predictions import Prediction
from .. import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    preds = Prediction.query.filter_by(user_id = current_user.id)
    return render_template('profile.html', user=current_user, predictions = preds)
  
  
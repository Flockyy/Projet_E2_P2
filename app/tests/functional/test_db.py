# fonctional/test_db.py

from app.tests.conftest import client
from app.models.users import User
from app.models.predictions import Prediction

def test_select_user(client):
	user = User.query.filter_by(id=1).first()
	assert user.email == 'mail@mail.com'

def test_select_prediction(client):
	pred = Prediction.query.filter_by(id=1).first()
	assert pred.fireplaces == 0
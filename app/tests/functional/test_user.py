# fonctional/test_user.py

from app.tests.conftest import client

def test_profile_page(client):
  
  response = client.get('/profile')
  assert response.status_code == 302
  
def test_prediction_page(client):
  response = client.get('/predict')
  assert response.status_code == 302
  

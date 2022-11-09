# fonctional/test_auth.py

from app.tests.conftest import client
from flask_login import login_user, current_user
from app.models.users import User

def test_login_status_code_ok(client):
  response = client.post('/signup', 
                        data={'email' : 'mail2@mail.com','name': 'Flocky', 'password' : 'test1234'}, 
                        headers = {'Content-Type': 'multipart/form-data'})
  
  user = User.query.filter_by(email='mail2@mail.com').first()
  assert user == User
  assert user.name == 'Flocky'
  assert user.password == 'test1234'
  assert response.status_code == 302
 
def test_login_status_code_ok(client):
  response = client.post('/login', 
                        data={'email' : 'mail@mail.com', 'password' : 'test1234'}, 
                        headers = {'Content-Type': 'multipart/form-data'})
  
  user = User.query.filter_by(email='mail@mail.com').first()
  login_user(user)
  
  assert response.status_code == 302
  assert current_user.email == 'mail@mail.com'
 
def test_logout_status_code_ok(client):
  response = client.get('/logout')
  assert response.status_code == 302

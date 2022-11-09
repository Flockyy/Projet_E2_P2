# fonctional/test_app.py

from app.tests.conftest import client

def test_index_should_status_code_ok(client):
	response = client.get('/')
	assert response.status_code == 200
 
def test_signup_should_status_code_ok(client):
	response = client.get('/signup')
	assert response.status_code == 200

def test_login_should_status_code_ok(client):
	response = client.get('/login')
	assert response.status_code == 200
 

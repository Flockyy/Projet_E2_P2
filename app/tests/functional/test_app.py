from app.tests.conftest import client

def test_index_should_status_code_ok(client):
	response = client.get('/')
	assert response.status_code == 200
 

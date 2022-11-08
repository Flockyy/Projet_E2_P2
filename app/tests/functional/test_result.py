from app.tests.conftest import client
from app.models.users import Prediction
import json

def test_index_should_status_code_ok(client):
  data = {
    'overallInteriorQuality' : '5',
    'totalSf': '6700',
    'garageArea': '730',
    'fireplaces': '0',
    'roomNbAbvGrd': '8',
    'overallExteriorQuality': '8',
    'fullLot': '11000',
    'timeBetweenSale': '0',
    'saleYear': '1961',
    'neighborhood': 'NAmes'
  }
  response = client.post('/result', data = data)
  assert response.status_code == 200
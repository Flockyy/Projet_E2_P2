from app.models.users import User
from app.models.users import Prediction

def test_new_user():
    user = User()
    user.email = 'test@gmail.com'
    user.password = 'test1234'
    user.name = 'user1'
    assert user.email == 'test@gmail.com'
    assert user.password != 'test12asdf34'
    assert user.name == 'user1'
    
def test_new_prediction():
    
    user = User()
    user.id = 0
    user.email = 'test@gmail.com'
    user.password = 'test1234'
    user.name = 'user1'
    
    pred = Prediction()
    pred.id = 0
    pred.user_id = user.id
    pred.overallInteriorQuality = 5
    pred.totalSf = 6700
    pred.garageArea = 730
    pred.fireplaces = 0 
    pred.roomNbAbvGrd = 8
    pred.overallExteriorQuality = 8
    pred.fullLot = 11000
    pred.timeBetweenSale = 0
    pred.saleYear = 1961
    pred.neighborhood = "NAmes"
    pred.result = 116407
    
    assert pred.id == 0
    assert pred.overallInteriorQuality == 5
    assert pred.totalSf == 6700
    assert pred.garageArea == 730
    assert pred.fireplaces == 0
    assert pred.roomNbAbvGrd ==8
    assert pred.overallExteriorQuality == 8
    assert pred.fullLot == 11000
    assert pred.timeBetweenSale == 0
    assert pred.saleYear == 1961
    assert pred.neighborhood != 1 
    assert pred.result == 116407

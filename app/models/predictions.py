from app import db

class Prediction(db.Model):
    __tablename__ = 'predictions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    overallInteriorQuality = db.Column(db.Integer)
    totalSf = db.Column(db.Integer)
    garageArea = db.Column(db.Integer)
    fireplaces = db.Column(db.Integer)
    roomNbAbvGrd = db.Column(db.Integer)
    overallExteriorQuality = db.Column(db.Integer)
    fullLot = db.Column(db.Integer)
    timeBetweenSale = db.Column(db.Integer)
    saleYear = db.Column(db.Integer)
    neighborhood = db.Column(db.String)
    result = db.Column(db.Integer)
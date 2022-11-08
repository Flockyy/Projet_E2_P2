from flask_login import UserMixin
from app import db
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base, UserMixin, db.Model):
    __tablename__ = "user_table"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
class Prediction(Base):
    __tablename__ = "prediction_table"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_table.id"))
    overallInteriorQuality = db.Column(db.Integer, db.ForeignKey(""))
    totalSf = db.Column(db.Integer, db.ForeignKey(""))
    garageArea = db.Column(db.Integer, db.ForeignKey(""))
    fireplaces = db.Column(db.Integer, db.ForeignKey(""))
    roomNbAbvGrd = db.Column(db.Integer, db.ForeignKey(""))
    overallExteriorQuality = db.Column(db.Integer, db.ForeignKey(""))
    fullLot = db.Column(db.Integer, db.ForeignKey(""))
    timeBetweenSale = db.Column(db.Integer, db.ForeignKey(""))
    saleYear = db.Column(db.Integer, db.ForeignKey(""))
    neighborhood = db.Column(db.String, db.ForeignKey(""))
    result = db.Column(db.Integer)
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SubmitField)
from wtforms.validators import InputRequired

class PredictionForm(FlaskForm):
    overallInteriorQuality = IntegerField('Overall interior quality', validators=[InputRequired()])
    totalSf = IntegerField('Total surface', validators=[InputRequired()])
    garageArea = IntegerField('Garage surface', validators=[InputRequired()])
    fireplaces = IntegerField('Fireplaces number', validators=[InputRequired()])
    roomNbAbvGrd = IntegerField('Room number of the above ground', validators=[InputRequired()])
    overallExteriorQuality = IntegerField('Overall exterior quality', validators=[InputRequired()])
    fullLot = IntegerField('Full lot surface', validators=[InputRequired()])
    timeBetweenSale = IntegerField('Time between house build and sale', validators=[InputRequired()])
    saleYear = IntegerField('Sale year', validators=[InputRequired()])
    neighborhood = StringField('Neighborhood name', validators=[InputRequired()])
    submit = SubmitField('Predict !')
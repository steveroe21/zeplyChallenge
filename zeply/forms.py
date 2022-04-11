from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class cryptoChoice(FlaskForm):
    BTC = StringField("BTC:")
    ETH = StringField("ETH")
    submit=SubmitField("Submit")


from bitcoinaddress import Wallet
from django.forms import CheckboxInput 
from flask import Flask, render_template
from database import get_db, close_db
from forms import cryptoChoice
from flask_session import Session


# Setting up App

app=Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Closing the database 

@app.teardown_appcontext
def close_db_at_end_of_request(e=None):
    close_db(e)



def generateAddress():
    wallet = Wallet(testnet= True)
    return wallet

# Default App Route

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cryptoChoice.html")
def cryptoChoice():
    form = cryptoChoice()
    if form.validate_on_submit():
        BTC = form.BTC.data
        ETH = form.ETH.data
        if BTC is CheckboxInput:
            BTC_address = generateAddress()
            BTC_id = id(BTC_address)
            db = get_db()
            if db.execute(""" SELECT * FROM BTC_addresses
                                WHERE BTC_id = ?;""", (BTC_id,)):
                return render_template("retrieve.html")
        else:
            if ETH is CheckboxInput:
                ETH_address = generateAddress()
                ETH_id = id(ETH_address)
                if db.execute(""" SELECT * FROM ETH_addresses
                                WHERE ETH_id = ?;""", (ETH_id,)):
                    return render_template("retrieve.html")

# List all previously made addresses from the database 

@app.route("/retrieve")
def retrieve():
    db = get_db()
    retrieve_BTC= db.execute("""SELECT * FROM BTC_addresses
                                WHERE BTC_id = ?;""").fetchall()
    retrieve_ETH= db.execute("""SELECT * FROM ETH_addresses
                                WHERE BTC_id = ?;""").fetchall()
    return render_template("retrieve.html", retrieve_BTC=retrieve_BTC, retrieve_ETH= retrieve_ETH )

# List the address and id for the user.

@app.route("/list.html")
def list():
    db = get_db()
    retrieve_BTC= db.execute("""SELECT * FROM BTC_addresses;""").fetchall()
    retrieve_ETH= db.execute("""SELECT * FROM ETH_addresses;""").fetchall()
    return render_template("list.html", retrieve_BTC=retrieve_BTC, retrieve_ETH= retrieve_ETH )

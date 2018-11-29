import sys
from flask import Flask, render_template,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/inpatient.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = automap_base(metadata=db.metadata)
engine = db.get_engine()
Base.prepare(engine, reflect=True)
Inpatient = Base.classes.inpatient
Drg = Base.classes.drg

@app.route("/")
def index():
    r"""Display the intro page"""
    return render_template("index.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route("/data")
def data():
    r"""Display the data page"""
    return render_template("data.html")

@app.route("/inpatient_data")
def inpatient_data():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).all()
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)

@app.route("/drg190")
def drg190():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).filter_by(drg_definition = '190 - CHRONIC OBSTRUCTIVE PULMONARY DISEASE W MCC')
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)


if __name__ == "__main__":
    app.run(debug=True)

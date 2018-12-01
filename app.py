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

@app.route("/question")
def question():
    return render_template("question")

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

@app.route("/drg119")
def drg119():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).filter_by(drg_definition = '190 - CHRONIC OBSTRUCTIVE PULMONARY DISEASE W MCC')
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)

@app.route("/drg119summary")
def drg119summary():
    r""" Returns a json summarizing medicare charges and patient discharges by hrr for 190 - CHRONIC OBSTRUCTIVE PULMONARY DISEASE W MCC'"""

    #query the database
    response = db.session.query(Inpatient).filter_by(drg_definition = '190 - CHRONIC OBSTRUCTIVE PULMONARY DISEASE W MCC')

    #iterate through the response to get a readable copy
    fils = []

    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        fils.append(rec)
    
    #feed the response into a DataFrame
    df = pd.DataFrame(fils)

    #build a function that will scrub the data to make it a proper number
    def sanitize(data):
        if type(data).__name__ != 'float':
            return (float( data.replace(",","")))
        else:
            return data

    #scrub the discharges column
    df['total_discharges'] = df['total_discharges'].apply(sanitize)

    #pivot the raw data into a summarized table
    summary = pd.pivot_table(df, index='hrr_description', values=['average_covered_charges', 'total_discharges'])

    #save pivot table to json
    return summary.reset_index().to_json(orient="records")

@app.route("/drg122")
def drg122():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).filter_by(drg_definition ='193 - SIMPLE PNEUMONIA & PLEURISY W MCC' )
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)

@app.route("/drg122summary")
def drg122summary():
    r""" Returns a json summarizing medicare charges and patient discharges by hrr for 193 - SIMPLE PNEUMONIA & PLEURISY W MCC'"""

    #query the database
    response = db.session.query(Inpatient).filter_by(drg_definition = '193 - SIMPLE PNEUMONIA & PLEURISY W MCC')

    #iterate through the response to get a readable copy
    fils = []

    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        fils.append(rec)
    
    #feed the response into a DataFrame
    df = pd.DataFrame(fils)

    #build a function that will scrub the data to make it a proper number
    def sanitize(data):
        if type(data).__name__ != 'float':
            return (float( data.replace(",","")))
        else:
            return data

    #scrub the discharges column
    df['total_discharges'] = df['total_discharges'].apply(sanitize)

    #pivot the raw data into a summarized table
    summary = pd.pivot_table(df, index='hrr_description', values=['average_covered_charges', 'total_discharges'])

    #save pivot table to json
    return summary.reset_index().to_json(orient="records")

@app.route("/drg123")
def drg123():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).filter_by(drg_definition = '194 - SIMPLE PNEUMONIA & PLEURISY W CC')
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)

@app.route("/drg123summary")
def drg123summary():
    r""" Returns a json summarizing medicare charges and patient discharges by hrr for 194 - SIMPLE PNEUMONIA & PLEURISY W CC'"""

    #query the database
    response = db.session.query(Inpatient).filter_by(drg_definition = '194 - SIMPLE PNEUMONIA & PLEURISY W CC')

    #iterate through the response to get a readable copy
    fils = []

    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        fils.append(rec)
    
    #feed the response into a DataFrame
    df = pd.DataFrame(fils)

    #build a function that will scrub the data to make it a proper number
    def sanitize(data):
        if type(data).__name__ != 'float':
            return (float( data.replace(",","")))
        else:
            return data

    #scrub the discharges column
    df['total_discharges'] = df['total_discharges'].apply(sanitize)

    #pivot the raw data into a summarized table
    summary = pd.pivot_table(df, index='hrr_description', values=['average_covered_charges', 'total_discharges'])

    #save pivot table to json
    return summary.reset_index().to_json(orient="records")

@app.route("/drg193")
def drg193():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).filter_by(drg_definition = '291 - HEART FAILURE & SHOCK W MCC')
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)

@app.route("/drg193summary")
def drg193summary():
    r""" Returns a json summarizing medicare charges and patient discharges by hrr for 291 - HEART FAILURE & SHOCK W MCC'"""

    #query the database
    response = db.session.query(Inpatient).filter_by(drg_definition = '291 - HEART FAILURE & SHOCK W MCC')

    #iterate through the response to get a readable copy
    fils = []

    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        fils.append(rec)
    
    #feed the response into a DataFrame
    df = pd.DataFrame(fils)

    #build a function that will scrub the data to make it a proper number
    def sanitize(data):
        if type(data).__name__ != 'float':
            return (float( data.replace(",","")))
        else:
            return data

    #scrub the discharges column
    df['total_discharges'] = df['total_discharges'].apply(sanitize)

    #pivot the raw data into a summarized table
    summary = pd.pivot_table(df, index='hrr_description', values=['average_covered_charges', 'total_discharges'])

    #save pivot table to json
    return summary.reset_index().to_json(orient="records")

@app.route("/drg194")
def drg194():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).filter_by(drg_definition = '292 - HEART FAILURE & SHOCK W CC')
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)

@app.route("/drg194summary")
def drg194summary():
    r""" Returns a json summarizing medicare charges and patient discharges by hrr for 292 - HEART FAILURE & SHOCK W CC'"""

    #query the database
    response = db.session.query(Inpatient).filter_by(drg_definition = '292 - HEART FAILURE & SHOCK W CC')

    #iterate through the response to get a readable copy
    fils = []

    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        fils.append(rec)
    
    #feed the response into a DataFrame
    df = pd.DataFrame(fils)

    #build a function that will scrub the data to make it a proper number
    def sanitize(data):
        if type(data).__name__ != 'float':
            return (float( data.replace(",","")))
        else:
            return data

    #scrub the discharges column
    df['total_discharges'] = df['total_discharges'].apply(sanitize)

    #pivot the raw data into a summarized table
    summary = pd.pivot_table(df, index='hrr_description', values=['average_covered_charges', 'total_discharges'])

    #save pivot table to json
    return summary.reset_index().to_json(orient="records")

@app.route("/drg261")
def drg261():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).filter_by(drg_definition = '392 - ESOPHAGITIS, GASTROENT & MISC DIGEST DISORDERS W/O MCC')
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)

@app.route("/drg261summary")
def drg261summary():
    r""" Returns a json summarizing medicare charges and patient discharges by hrr for 392 - ESOPHAGITIS, GASTROENT & MISC DIGEST DISORDERS W/O MCC'"""

    #query the database
    response = db.session.query(Inpatient).filter_by(drg_definition = '392 - ESOPHAGITIS, GASTROENT & MISC DIGEST DISORDERS W/O MCC')

    #iterate through the response to get a readable copy
    fils = []

    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        fils.append(rec)
    
    #feed the response into a DataFrame
    df = pd.DataFrame(fils)

    #build a function that will scrub the data to make it a proper number
    def sanitize(data):
        if type(data).__name__ != 'float':
            return (float( data.replace(",","")))
        else:
            return data

    #scrub the discharges column
    df['total_discharges'] = df['total_discharges'].apply(sanitize)

    #pivot the raw data into a summarized table
    summary = pd.pivot_table(df, index='hrr_description', values=['average_covered_charges', 'total_discharges'])

    #save pivot table to json
    return summary.reset_index().to_json(orient="records")

@app.route("/drg310")
def drg310():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).filter_by(drg_definition = '470 - MAJOR JOINT REPLACEMENT OR REATTACHMENT OF LOWER EXTREMITY W/O MCC')
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)

@app.route("/drg310summary")
def drg310summary():
    r""" Returns a json summarizing medicare charges and patient discharges by hrr for 470 - MAJOR JOINT REPLACEMENT OR REATTACHMENT OF LOWER EXTREMITY W/O MCC'"""

    #query the database
    response = db.session.query(Inpatient).filter_by(drg_definition = '470 - MAJOR JOINT REPLACEMENT OR REATTACHMENT OF LOWER EXTREMITY W/O MCC')

    #iterate through the response to get a readable copy
    fils = []

    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        fils.append(rec)
    
    #feed the response into a DataFrame
    df = pd.DataFrame(fils)

    #build a function that will scrub the data to make it a proper number
    def sanitize(data):
        if type(data).__name__ != 'float':
            return (float( data.replace(",","")))
        else:
            return data

    #scrub the discharges column
    df['total_discharges'] = df['total_discharges'].apply(sanitize)

    #pivot the raw data into a summarized table
    summary = pd.pivot_table(df, index='hrr_description', values=['average_covered_charges', 'total_discharges'])

    #save pivot table to json
    return summary.reset_index().to_json(orient="records")

@app.route("/drg440")
def drg440():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).filter_by(drg_definition = '690 - KIDNEY & URINARY TRACT INFECTIONS W/O MCC')
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)

@app.route("/drg440summary")
def drg440summary():
    r""" Returns a json summarizing medicare charges and patient discharges by hrr for 690 - KIDNEY & URINARY TRACT INFECTIONS W/O MCC'"""

    #query the database
    response = db.session.query(Inpatient).filter_by(drg_definition = '690 - KIDNEY & URINARY TRACT INFECTIONS W/O MCC')

    #iterate through the response to get a readable copy
    fils = []

    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        fils.append(rec)
    
    #feed the response into a DataFrame
    df = pd.DataFrame(fils)

    #build a function that will scrub the data to make it a proper number
    def sanitize(data):
        if type(data).__name__ != 'float':
            return (float( data.replace(",","")))
        else:
            return data

    #scrub the discharges column
    df['total_discharges'] = df['total_discharges'].apply(sanitize)

    #pivot the raw data into a summarized table
    summary = pd.pivot_table(df, index='hrr_description', values=['average_covered_charges', 'total_discharges'])

    #save pivot table to json
    return summary.reset_index().to_json(orient="records")

@app.route("/drg517")
def drg517():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).filter_by(drg_definition = '871 - SEPTICEMIA OR SEVERE SEPSIS W/O MV >96 HOURS W MCC')
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)

@app.route("/drg517summary")
def drg517summary():
    r""" Returns a json summarizing medicare charges and patient discharges by hrr for 690 - 871 - SEPTICEMIA OR SEVERE SEPSIS W/O MV >96 HOURS W MCC'"""

    #query the database
    response = db.session.query(Inpatient).filter_by(drg_definition = '871 - SEPTICEMIA OR SEVERE SEPSIS W/O MV >96 HOURS W MCC')

    #iterate through the response to get a readable copy
    fils = []

    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        fils.append(rec)
    
    #feed the response into a DataFrame
    df = pd.DataFrame(fils)

    #build a function that will scrub the data to make it a proper number
    def sanitize(data):
        if type(data).__name__ != 'float':
            return (float( data.replace(",","")))
        else:
            return data

    #scrub the discharges column
    df['total_discharges'] = df['total_discharges'].apply(sanitize)

    #pivot the raw data into a summarized table
    summary = pd.pivot_table(df, index='hrr_description', values=['average_covered_charges', 'total_discharges'])

    #save pivot table to json
    return summary.reset_index().to_json(orient="records")

@app.route("/drg518")
def drg518():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).filter_by(drg_definition = '872 - SEPTICEMIA OR SEVERE SEPSIS W/O MV >96 HOURS W/O MCC')
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        d_list.append(rec)
    return jsonify(d_list)

@app.route("/drg518summary")
def drg518summary():
    r""" Returns a json summarizing medicare charges and patient discharges by hrr for 872 - SEPTICEMIA OR SEVERE SEPSIS W/O MV >96 HOURS W/O MCC'"""

    #query the database
    response = db.session.query(Inpatient).filter_by(drg_definition = '872 - SEPTICEMIA OR SEVERE SEPSIS W/O MV >96 HOURS W/O MCC')

    #iterate through the response to get a readable copy
    fils = []

    for r in response:
        rec = r.__dict__.copy()
        del rec['_sa_instance_state']
        fils.append(rec)
    
    #feed the response into a DataFrame
    df = pd.DataFrame(fils)

    #build a function that will scrub the data to make it a proper number
    def sanitize(data):
        if type(data).__name__ != 'float':
            return (float( data.replace(",","")))
        else:
            return data

    #scrub the discharges column
    df['total_discharges'] = df['total_discharges'].apply(sanitize)

    #pivot the raw data into a summarized table
    summary = pd.pivot_table(df, index='hrr_description', values=['average_covered_charges', 'total_discharges'])

    #save pivot table to json
    return summary.reset_index().to_json(orient="records")

if __name__ == "__main__":
    app.run(debug=True)
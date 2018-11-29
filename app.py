import sys
from flask import Flask, render_template,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jsglue import JSGlue
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)
jsglue = JSGlue(app)

#app.config['STATIC_FOLDER'] = 'static'
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
    #res = db.session.query(Inpatient).all()
    return render_template("data.html")

@app.route("/inpatient_data")
def inpatient_data():
    r""" Returns a json of the inpatient data"""

    response = db.session.query(Inpatient).all()
    d_list = []
    for r in response:
        rec = r.__dict__.copy()
        d_list.append(rec)
    return jsonify(d_list)
        

	
# @app.route("/data")
# def data():
#     r"""Display the data table plot"""
#     res = db.session.query(Inpatient).all()

#     return render_template("data.html",xpage="Data")
	
# @app.route("/drg_names")
# def names():
#     """Return a list of sample names."""
#     # Use Pandas to perform the sql query
#     stmt = db.session.query(Drg).statement
#     df = pd.read_sql_query(stmt, db.session.bind)
#     print(df.head())
	
#     # Return a list of the column names (sample names)
#     return jsonify(list(df.columns)[:])

# @app.route("/get_inpatient_data")
# def inpatient_data():
#     r""" This function returns the list of all inpatient 
#     data """
    
#     res = db.session.query(Inpatient).all()

#     dlist = []
#     for dset in res:
#         md = dset.__dict__.copy()
#         del md['_sa_instance_state']
#         dlist.append(md)
    
#     return jsonify(dlist)

# @app.route("/drg_list/<drg_definition>")
# def sample_metadata(drg_definition):
#     """Return the metadata for a given DRG name."""
#     sel = [
#         Drg.drg_id, 
# 		Drg.drg_definition,
# 		Drg.drg_code,
# 		Drg.drg_description,
#     ]

#     results = db.session.query(*sel).filter(Drg.drg_definition == drg_definition).all()

#     # Create a dictionary entry for each row of metadata information
#     sample_metadata = {}
#     for result in results:
#         sample_metadata["id"] = result[0]
#         sample_metadata["drg_definition"] = result[1]
#         sample_metadata["drg_code"] = result[2]
#         sample_metadata["drg_description"] = result[3]

#     print(sample_metadata)
#     return jsonify(sample_metadata)   
	
if __name__ == "__main__":
    app.run(debug=True)

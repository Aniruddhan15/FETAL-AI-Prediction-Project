from flask import Flask,request, render_template
import numpy as np
import pandas as pd
import pickle

model=pickle.load(open(r'fetal_health1.pkl','rb'))
app-Flask (name)


@app.route("/")
def f():
return render_template("index.html")
@app.route("/home", methods=["GET", "POST"])

def home():

prolongued decelerations float(request.form['prolongued decelerations'])

abnormal_short_term_variability float (request.form['abnormal_short_term variability']) percentage_of_time_with_abnormal_long term_variability float(request.form['percentage of time'])

histogram variance float(request.form['histogram variance']) histogram median float(request.fowl'histogram_median'])

mean_value_of_long_term_variability float(request.form['mean_value_of_long_term_variability'])

histogram mode 
float(request.form['histogram_mode']) accelerations float(request.form['accelerations'])

x= [[prolongued_decelerations, abnormal_short_term_variability, percentage_of_time_with abnormal]]

output=model.predict(x)

out=['Normal','Pathological','Suspect']

if int (output[0])--0:

output='Normal elif int (output[0]) 1:

output=Pathological

else: output='Suspect

return render_template('output.html',output=output)


if name "main : 21 app.run(debug=True)
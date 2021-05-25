# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 21:53:31 2021

@author: shruthi
"""

from flask import Flask, redirect, url_for, render_template,request

app = Flask(__name__) 

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        if request.form.get("tour"):
            return redirect(url_for('dest'))
        elif request.form.get("hotel"):
            return redirect(url_for('hotel'))
            
    return render_template("index.html")

@app.route("/dest")
def dest():
    return render_template("dest.html")


@app.route("/hotel")
def hotel():
    return render_template("ootyhotels.html")

if __name__ == "__main__":
    app.run()
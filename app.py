from flask import Flask , render_template,app,request
import pandas as pd
import numpy as np
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
# @app.route("/predict",methods = ['POST'])
# def predict():
#     data = request.json['json']
#     print(data)
if __name__ == "__main__":
    app.run(debug = True)

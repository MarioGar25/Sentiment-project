from flask import Flask 
from bson import json_util, ObjectId
from helper_utils.endpoints import get_col, col_name, col_group, col_message, insert_new, sentiment_analisys, polarity_analisys, sentimental_mean
from flask import request

app = Flask("Sentimental Valuetor API")

@app.route("/")
def root():
    return f"Welcome to the Sentimental Valuetor APi. Collections Avaibles: users, groups, messages"

@app.route("/<col>")
def show_col(col):
    return get_col(col)

@app.route("/<col>/showbygroup/<group>")
def show_col_group(col, group):
    return col_group(col, group)

@app.route("/<col>/showbymessage/<message>")
def show_col_message(col, message):
    return col_message(col, message)

@app.route("/<col>/showbyname/<name>")
def show_col_name(col, name):
    return col_name(col, name)

@app.route("/<col>/insert")
def insert(col):
    args = dict(request.args)
    return insert_new(col, args)

@app.route("/sentimentalAnalisys/<string>")
def sent_an(string):
    return sentiment_analisys(string)

@app.route("/polarityAnalisys/<string>")
def pol_an(string):
    return polarity_analisys(string)

@app.route("/sentimentalAnalisys/mean")
def sent_mean():
    args = dict(request.args)
    return sentimental_mean(args)


app.run(debug=True)
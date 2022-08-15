from pickle import FALSE
from flask import Flask, render_template, jsonify
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbMovieStar


import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/star', methods=["GET"])
def star_api():
  stars = list(db.movie_star.find({}, {'_id': 0}))
  return jsonify({'result':'success', 'msg': 'Connected', 'data' : stars})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
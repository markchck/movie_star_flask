from pickle import FALSE
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import pdb
client = MongoClient('localhost', 27017)
db = client.dbMovieStar

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/star', methods=["GET"])
def star_api():
  stars = list(db.movie_star.find({}, {'_id': 0}).sort('like', -1))
  # stars = list(db.movie_star.find({}, {'_id': 0}))
  return jsonify({'result':'success', 'msg': 'Connected', 'data' : stars})

@app.route('/star', methods=["POST"])
def post_api():
  id_received = request.form["id"]
  target_star = db.movie_star.find_one({'id': int(id_received)}, {'_id':False})

  new_like = target_star["like"]+1
  db.movie_star.update_one({'id':int(id_received)}, {'$set':{'like':new_like}})
  # pdb.set_trace()
  return jsonify({'result':'success'})
  
if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
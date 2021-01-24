from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo
from secret import databasepw

import random


app = Flask(__name__)

dbname = "mondeenchiffres"
app.config['MONGO_DBNAME'] = dbname
app.config["MONGO_URI"] = f"mongodb+srv://user:{databasepw}@cluster0.cxs4c.mongodb.net/{dbname}?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/country', methods=['GET'])
def getAllCountry():
  country = mongo.db.test
  output = []
  for c in country.find():
    output.append({'country' : c['country'], 'pop' : c['pop'], 'density' : c['density']})
  return jsonify({'result' : output})


@app.route('/country/<name>', methods=['GET'])
def getOneCountry(name):
  country = mongo.db.test
  c = country.find_one({'country' : name})
  print(c)
  if c:
    output = {'country' : c['country'], 'pop' : c['pop'], 'density' : c['density']}
  else:
    output = "Country not found"
  return jsonify({'result' : output})


@app.route('/addcountry/<name>', methods=['GET'])
def addCountry(name):
        density = random.randint(10, 1000)
        _id = random.randint(1000, 1000000000)
        pop = random.randint(10000, 10000000)
        
        country={"_id":_id,
                    "country": name, 
                    "pop": pop,
                    "density": density
                    }

        mongo.db.test.insert_one(country)

        return mongo.db.test.find_one({'country': name})




@app.route('/category/<cat>', methods=['GET'])
def getCategory(cat):
  if int(cat) == 1:
    b1 = 0
    b2 = 200
  if int(cat) == 2:
    b1 = 200
    b2 = 400
  if int(cat) == 3:
    b1 = 400
    b2 = 1200
  if int(cat) == 4:
    b1 = 1200
    b2 = 1000000
  output =[]
  country = mongo.db.test
  collection = country.find({'density' :  {"$gt" : b1, "$lt" : b2} })
  print(collection)
  try:
    for c in collection:
      output.append({'country' : c['country'], 'pop' : c['pop'], 'density' : c['density']})
  except:
    output = "Country not found"
  return jsonify({'result' : output})

  
if __name__ == '__main__':
    app.run(debug=True)

import pymongo

from flask import Flask
from flask import request,jsonify
from flask_cors import CORS

myclient = pymongo.MongoClient("mongodb://localhost:27017")  # To connect with mongodb 
mydb =myclient['employee'] # your database name
mycul = mydb['program']    #your collection name


app = Flask(__name__)
cors = CORS(app)
app.config["CORS _HEADERS"] = "Content-Type"

# Create(Post/Push) - This is used for Add data in database 
@app.route("/Create", methods = ["Post","Get"])
def Create():
    content = request.get_json()
    mycul.insert_one(content)
    return"Push initiated"

# Update(Put) - This is used for update something in database
@app.route("/Update", methods = ["Post","Get"])
def Update():
    content = request.get_json()
    print (content )
    myval = {"$set":{"Score":content['Score'],"Sub":content['Sub']}}
   # myval = {"$set":{"Sub":content['Sub']}}
    mycul.update_one({"Name":content["Name"]}, myval)
    return"Update initiated"

# Delete - for delete something in database
@app.route("/Delete", methods = ["Post","Get"])
def Delete():
    content = request.get_json()
    mycul.delete_one({"Name":content["Name"]})
    return"Delete initiated"

# Pulling(Read/Get) - To read data from database
@app.route("/Pulling", methods = ["Post","Get"])
def Pull():
    content = request.get_json()
    ViewQuery = []
    PulledData = mycul.find({"Name":content["Name"]})
    for i in PulledData:
        ViewQuery.append({"Name":i["Name"],"Score":i["Score"],"Sub":i['Sub']})
    return jsonify(ViewQuery)
    
if __name__ =="__main__":
    app.run()

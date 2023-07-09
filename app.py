from flask import Flask,request,jsonify,make_response
from flask_restful import Resource,Api
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
import json

uri = "mongodb+srv://Abbas:yellowyellow@cluster0.bqqrivd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

db=client['Cluster0']

coll=db['crud-api']

app=Flask(__name__)


api= Api(app)

class call(Resource):
    def get(self):
        # ans=dict()
        # i=0
        ans=[]
        for data in coll.find():
            ans.append({'_id':data['_id'],
                        'name':data['name'],
                        'email':data['email'],
                        'password':data['password']})
            
          
        return jsonify(json.loads(json.dumps(ans)))


    
        
    def post(self):
        # id=int(input("id:"))
        # name=input("name:")
        # email=input("email:")
        # password=input("password:")
        try:
            data=request.get_json()
            json={'_id':data['_id'],'name':data['name'],'email':data['email'],'password':data['password']}
            coll.insert_one(json)
            return jsonify({"message":"Record Added"})
        except:
            return jsonify({"message":"Error"})

    

class calltwo(Resource):
    def get(self,id):
        
        try:
            
            for data in coll.find({'_id':id}):
                ans={'_id':data['_id'],'name':data['name'],'email':data['email'],'password':data['password']}
            return jsonify(ans)
        except:
            return jsonify({"message":"id not found"})
            
            
          
        
        
    def delete(self,id):
        try:
            json={'_id':id}
            coll.delete_one(json)
            return jsonify({"message":"Record Deleted"})
        except:
            return jsonify({"message":"id not found"})
            
        
    def put(self,id):
        try:
            data=request.get_json()
            old= coll.find({'_id':id})
            for x in old:
                oldvalue=x
                new = { "$set": {'name':data['name'],'email':data['email'],'password':data['password']}}
                coll.update_one(oldvalue, new)
            
            
            return jsonify({"message":"Updated"})
        
        except:
            return jsonify({"message":"id not found"})
        
        

api.add_resource(call,'/users')
api.add_resource(calltwo,'/users/<int:id>')


if __name__=='__main__':
    app.run(debug=True)

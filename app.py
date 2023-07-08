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
        for x in coll.find():
            ans.append(json.dumps(x))
            
          
        return make_response(jsonify(json.dumps(ans,indent=0)))


    
        
    def post(self):
        # id=int(input("id:"))
        # name=input("name:")
        # email=input("email:")
        # password=input("password:")
        data=request.get_json()
        json={'_id':data['_id'],'name':data['name'],'email':data['email'],'password':data['password']}
        coll.insert_one(json)
        
    

class calltwo(Resource):
    def get(self,id):
        ans=[]
        for x in coll.find({'_id':id}):
            ans.append(x)
            
          
        return json.dumps(ans,indent=0)
        
    def delete(self,id):
        json={'_id':id}
        coll.delete_one(json)
    def put(self,id):
        
        name=input("name:")
        email=input("email:")
        password=input("password:")
        old= coll.find({'_id':id})
        new = { "$set": {'name':name,'email':email,'password':password} }
        coll.update_one(old, new)

#     def get(self,id):
#         pass

# class POST(Resource):
#     def post(self):
#         pass


# class PUT(Resource):
#     def delete(self):
#         pass


# class DELETE(Resource):
#     def delete(self):
#         pass











api.add_resource(call,'/users')
api.add_resource(calltwo,'/users/<int:id>')


if __name__=='__main__':
    app.run(debug=True)

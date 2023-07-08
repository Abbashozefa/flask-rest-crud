from flask import Flask,request
from flask_restful import Resource,Api
import pymongo




app=Flask(__name__)


api= Api(app)

class call(Resource):
    def get(self):
        pass


    def get(self,id):
        pass
    def post(self):
        pass
    def delete(self):
        pass
    def delete(self):
        pass


class GET(Resource):
    def get(self):
        pass


    def get(self,id):
        pass

class POST(Resource):
    def post(self):
        pass


class PUT(Resource):
    def delete(self):
        pass


class DELETE(Resource):
    def delete(self):
        pass











api.add_resource(call,'/users')
api.add_resource(POST,'/users')
api.add_resource(PUT,'/users')
api.add_resource(DELETE,'/users')

if __name__=='__main__':
    app.run(debug=True)

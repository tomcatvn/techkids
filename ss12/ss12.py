from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from mongoengine import *
import json

connect(
   'thanhku',
   username = '8f8f8f8',
   password = '123456',
   host = 'ds135798.mlab.com',
   port = 35798
)

app = Flask(__name__)
api = Api(app)

class Phim12(Document):
    tenphim = StringField()
    theloai = StringField()
    thoiluong = StringField()

parser = reqparse.RequestParser()
parser.add_argument("tenphim",type=str)
parser.add_argument("theloai", type=str)
parser.add_argument("thoiluong",type=str)


class Phim1(Resource):
    def get(self):
        return [json.loads(phim.to_json()) for phim in Phim12.objects]
    def post(self):
        arg = parser.parse_args()
        tenphim = arg["tenphim"]
        theloai = arg["theloai"]
        thoiluong = arg["thoiluong"]
        phim = Phim12(tenphim= tenphim,theloai=theloai,thoiluong=thoiluong)
        phim.save()
        return "posted"

class Phim2(Resource):
    def delete(self,id):
        phim = Phim12.objects.with_id(id)
        phim.delete()
        return "deleted"
    def put(self,id):
        phim= Phim12.objects.with_id(id)
        arg = parser.parse_args()
        tenphim = arg["tenphim"]
        theloai = arg["theloai"]
        thoiluong = arg["thoiluong"]
        phim.update(set__tenphim = tenphim, set__theloai = theloai, set__thoiluong = thoiluong)

        return "updated"


api.add_resource(Phim1,'/api/phim')
api.add_resource(Phim2,'/api/phim/<string:id>')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port="2828")

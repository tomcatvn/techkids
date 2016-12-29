from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from mongoengine import *
import json

parser = reqparse.RequestParser()
parser.add_argument("name",type=str, location = "json")
parser.add_argument("desc",type=str, location = "json")
parser.add_argument("img",type=str, location = "json")

connect(
   'thanhku',
   username = '8f8f8f8',
   password = '123456',
   host = 'ds135798.mlab.com',
   port = 35798
)


app = Flask(__name__)
api = Api(app)

class Zodiac(Document):
    name = StringField()
    desc = StringField()
    img = StringField()

def me2json(item):
    return json.loads(item.to_json())

def melist2json(list):
    return [me2json(item) for item in list]


@app.route('/')
def hello_world():
    return 'Hello World!'

hrc_list = [
    "Nhân Mã"," Yêu đời, Phởn"
]

class HrcListRes(Resource):
    def get(self):
        return [json.loads(zodiac.to_json()) for zodiac in Zodiac.objects]
    def post(self):
        args = parser.parse_args()
        name = args["name"]
        desc = args["desc"]
        img = args["img"]
        zodiac = Zodiac(name=name, desc=desc, img=img)
        zodiac.save()
        return json.loads(zodiac.to_json(),404)

class HrcRes(Resource):
    def get(self,hrc_id):
        return json.loads(Zodiac.objects().with_id(hrc_id).to_json())
    def delete(self, hrc_id):
        Zodiac.objects().with_id(hrc_id).delete()
        return {"code":1, 'status':'ok'},200
    def put(self,hrc_id):
        zodiac = Zodiac.objects().with_id(hrc_id)
        args = parser.parse_args()
        name = args["name"]
        desc = args["desc"]
        img = args["img"]
        zodiac.update(set__name = name, set__desc=desc, set__img= img)

        return json.loads(Zodiac.objects().with_id(hrc_id).to_json())


api.add_resource(HrcListRes,"/api/hrc")
api.add_resource(HrcRes,"/api/hrc/<hrc_id>")
if __name__ == '__main__':
    app.run()

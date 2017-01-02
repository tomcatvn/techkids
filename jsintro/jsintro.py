from flask import Flask,render_template
import json
from flask_restful import Resource, Api
from nocache import nocache

app = Flask(__name__)

api = Api(app)
class FoodResource(Resource):
    def get(self):
        return {"name":"Long lon","desc":"ahihihihhi"}


api.add_resource(FoodResource,"/api/food")

@app.route('/')
def jsjs():
    return render_template('index.html')

@app.route('/cunghoangdao')
def cunghoangdao():
    return render_template("cunghoangdao.html")

@app.route('/ajax')
@nocache
def ajax():
    return render_template('ajax.html')

if __name__ == '__main__':
    app.run(port=2828)

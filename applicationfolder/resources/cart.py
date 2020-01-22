from flask_restful import Resource
from flask import *
from common.utils import *
import pymysql.cursors

class Cart(Resource):
    def post(self):
        pass
    def get(self):
        data=json.loads(request.args.get('data'))
        for key,value in data.items():
            data[key][0] = int(data[key][0])
            data[key][1] = int(data[key][1])
        username = session['username']
        print(data,username)
        return output_html(render_template('cart.html',data=data,username=username),200)


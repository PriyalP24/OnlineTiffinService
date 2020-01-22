from flask_restful import Resource
from flask import *
from common.utils import *

class Send_SignIn(Resource):
    def post(self):
        return output_html(render_template('signin.html'),200)
    def get(self):
        return output_html(render_template('signin.html'),200)

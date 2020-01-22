from flask_restful import Resource
from flask import *
from common.utils import *


class Index(Resource):
    def get(self):
        return output_html(render_template('index.html'),200)
    def post(self):
        return output_html(render_template('index.html'),200)


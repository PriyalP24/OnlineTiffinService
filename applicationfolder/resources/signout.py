from flask_restful import Resource
from flask import *
from common.utils import *

class SignOut(Resource):
    def get(self):
        if 'username' in session:
            session.pop('username', None)
            flash('You have successfully logged out.')
        return output_html(render_template('signin.html'),200)
    def post(self):
        if 'username' in session:
            session.pop('username', None)
            flash('You have successfully logged out.')
        return output_html(render_template('signin.html'),200)
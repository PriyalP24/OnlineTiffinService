import pymysql.cursors
from datetime import timedelta
from flask import *
from flask_restful import Resource,Api,reqparse


app = Flask(__name__)
app.secret_key = 'any random string'






if __name__ == '__main__':
    app.run(debug=True)

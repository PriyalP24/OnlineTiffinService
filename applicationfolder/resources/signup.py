from flask_restful import Resource
from flask import *
from applicationfolder.main.config import Config
import pymysql.cursors

from applicationfolder.common.utils import *

app = Flask(__name__)
app.secret_key = 'any random string'
class SignUp(Resource):
    def post(self):
        connection = pymysql.connect(
                                host='localhost',
                                user='root',
                                password='root123',
                                db='users',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

        name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `users` (username,email,password) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, email, password))
                connection.commit()
                connection.close()
                return output_html(render_template('signin.html'),200)
        except Exception as e:
            print(str(e))
            return output_html(render_template('signup.html'),200)



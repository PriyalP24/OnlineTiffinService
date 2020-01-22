from flask_restful import Resource
from flask import *
from applicationfolder.main.config import Config
import pymysql.cursors
from datetime import timedelta
from applicationfolder.common.utils import *

app = Flask(__name__)
app.secret_key = 'any random string'

class Signin(Resource):
    def post(self):
        session.permanent = True
        app.PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)
        connection = pymysql.connect(
                                host='localhost',
                                user='root',
                                password='root123',
                                db='users',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

        error = None
        try:
            with connection.cursor() as cursor:
                sql = "SELECT `username`, `password` FROM `users` WHERE `username`=%s and `password`=%s"
                cursor.execute(sql, (request.form["username"], request.form['password']))
                result = cursor.fetchone()
                if result:
                    session['username'] = request.form['username']
                    username = session['username']
                    connection = pymysql.connect(
                        host='localhost',
                        user='root',
                        password='root123',
                        db='cart',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
                    with connection.cursor() as cursor:
                        sql = "SELECT * FROM item"
                        cursor.execute(sql, ())
                        menu = cursor.fetchall()
                        data = {'username': request.form['username'],'menu': menu}
                    return output_html(render_template('home.html', data=data,username=username),200)
                else:
                    error = 'Invalid username or password. Please try again!'
                    return output_html(render_template('signin.html', error=error),200)
        except Exception as e:
            print(str(e))
            return output_html(render_template('signin.html', error=error),200)




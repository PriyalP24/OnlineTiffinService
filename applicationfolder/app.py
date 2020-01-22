from flask import *
from flask_restful import Api
from datetime import timedelta
from applicationfolder.resources.signin import Signin
from applicationfolder.resources.signup import SignUp
from applicationfolder.resources.signout import SignOut
from applicationfolder.resources.index import Index
from applicationfolder.resources.cart import Cart
from applicationfolder.resources.send_signin import Send_SignIn
from applicationfolder.resources.send_signup import Send_SignUp


app = Flask(__name__)
api = Api(app)
app.secret_key = 'any random string'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)

api.add_resource(Index ,'/')
api.add_resource(Signin, '/signin')

api.add_resource(Send_SignIn ,'/send_signin')
api.add_resource(Send_SignUp ,'/send_signup')
api.add_resource(SignOut,'/signout')
api.add_resource(SignUp, '/signup')
api.add_resource(Cart, '/cart')

if __name__ == '__main__':
    app.run(debug=True)
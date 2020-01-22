from flask import *
app = Flask(__name__)
app.secret_key = 'any random key'

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
            return render_template('login.html', error=error)

        else:
            flash("You were successfully logged in")
            return redirect(url_for('index'))
    return render_template('login.html', error=error)




if __name__=='__main__':
    app.run(debug=True)
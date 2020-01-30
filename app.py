from flask import *
from databases import *
from flask import session as login_session
app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


# routes 


# signin
@app.route('/')
def home():
	return signup()
	# return render_template("home.html")

@app.route('/add', methods=['GET', 'POST'])
def signup():
		if request.method == 'GET':
			return render_template('signup.html')
		else:

			name = request.form['user_name']
			year = request.form['user_year']
			add_user(name,year,0)
			login_session["username"]=name
			return redirect('/user/' + name)		


@app.route('/body',methods=['GET','POST'])
def about():
	if 'username' in login_session:
		return render_template("body.html",username=login_session['username'])
	print("You're not logged in. You can't enter body.html")
	return redirect(url_for('signup'))
	


@app.route('/user/<string:user_name>')
def display_user(user_name):
    return render_template('user.html', user=query_by_name(user_name))

@app.route('/immune_system')
def Immune():
	return render_template('imm.html')

@app.route('/nervous_system')
def nervous():
	return render_template('nervous.html')

# //////////////////////



if __name__ == '__main__':
    app.run(debug=True)

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'al'}
	posts =[
	{'author': {'username':'ana'},
	 'body':'Beautiful day at beach'
	},
	{'author':{'username':'ali'},
	'body':'The Avengers Day'
	}
	]


	return render_template('index.html',title='Home', user=user,posts=posts)
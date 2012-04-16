

from flask import Blueprint


mod = Blueprint('welcome', __name__, url_prefix='')

@mod.route('/')
def welcome():
	return  "Welcome to my humble place"

@mod.route('/hello/', methods=['GET', 'POST'])
def hello():
	return  "Why, hello little brown mouse"

@mod.route('/bye/')
def bye():
	return  "Bye now!"
from flask import Blueprint

views = Blueprint('views', __name__)



@views.route('/')
def home():
    return 'This is the Whale Coffee Home Page'


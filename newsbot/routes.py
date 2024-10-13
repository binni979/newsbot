
from newsbot import application
from flask import render_template

@application.route('/')
def index():
    return 'Hello, World!'
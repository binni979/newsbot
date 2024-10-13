from flask import Flask

application = Flask(__name__)

from newsbot import routes
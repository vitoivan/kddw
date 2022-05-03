
from flask import Flask

def init_app(app: Flask):

	from . import smtp

	smtp.init_app(app)
from flask import Flask

def create_app():
	app = Flask(__name__)

	from . import configs, blueprints, services

	configs.init_app(app)
	blueprints.init_app(app)
	services.init_app(app)

	return app
from flask import Flask

def init_app(app: Flask):

	from . import database, env, migrations, jwt

	env.init_app(app)
	database.init_app(app)
	jwt.init_app(app)
	migrations.init_app(app)

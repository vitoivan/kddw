from flask import Flask

def init_app(app: Flask):
    
	from .user_blueprints import user_bp
	from .admin_blueprints import admin_bp
	from .playlist_blueprints import playlist_bp

	app.register_blueprint(user_bp)
	app.register_blueprint(admin_bp)
	app.register_blueprint(playlist_bp)

	return app
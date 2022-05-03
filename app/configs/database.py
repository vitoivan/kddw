from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def init_app(app: Flask):

	db.init_app(app)
	app.db = db

	#import models
	from app.models.user import UserModel
	from app.models.youtube import YoutubeModel 
	from app.models.playlist import PlaylistModel
	from app.models.videos import VideoModel
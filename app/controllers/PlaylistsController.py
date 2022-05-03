from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, current_app, request
from .utils import validate_request
from app.middlewares.is_staff import is_staff

from app.models.playlist import PlaylistModel
from app.models.videos import VideoModel
from app.models.user import UserModel
from app.models.errors import BadRequest
from app.controllers.VideosController import VideosController




class PlaylistController:

	@staticmethod	
	def is_more_badass(query):
		user = UserModel.query.get(query.owner)
		if not user:
			return False
		staff_level_from_token = get_jwt_identity().get('staff_level')
		if staff_level_from_token is None or staff_level_from_token is False:
			return False
		return staff_level_from_token < user.staff_level

	@classmethod
	def register_videos(cls, videos, session):
		all_videos = []
		try:
			for video in videos:
				validate_request(video, ['youtube', 'title', 'description'])
				all_videos.append(VideoModel(**video))
			for video in all_videos:
				session.add(video)

		except BadRequest as e:
			msg = {
				'message': 'Invalid video format',
				'expected': ['youtube', 'title', 'description']
			}
			raise BadRequest(msg) 
		
	@classmethod
	@jwt_required()
	@is_staff
	def register(cls):
		body = request.get_json()
		session = current_app.db.session
		valid_keys = ['title','description','videos']
		try:
			validate_request(body, valid_keys)
			videos = body.pop('videos')
			videos = VideosController.register(videos, session)
			data = {**body, 'owner': get_jwt_identity().get('id')}
			query = PlaylistModel(**data, videos=videos)
			session.add(query)
			session.commit()
			return jsonify(query), 201
		except BadRequest as e:
			return jsonify(e.msg), e.status

	@classmethod
	@jwt_required()
	@is_staff
	def delete(cls, id: int):

		session = current_app.db.session
		query = PlaylistModel.query.get(id)
		if not query:
			return {'message': 'Playlist not found'}, 404 
		is_owner = get_jwt_identity().get('id') == query.owner
		if not is_owner and not cls.is_more_badass(query):
			return {'message': 'Unauthorized.'}, 401
		session.delete(query)
		session.commit()
		return '', 201

	@classmethod
	def get(cls):
		query = PlaylistModel.query.all()
		return jsonify(query), 200
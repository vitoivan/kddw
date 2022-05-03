from flask import current_app, jsonify, request
from flask_jwt_extended.utils import create_access_token, get_jwt_identity
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError
from app.models.errors import BadRequest
import datetime
from app.models.user import UserModel
from .utils import validate_request


class UserController:
	
	@classmethod
	@jwt_required()
	def register(cls):

		body = request.get_json()
		session = current_app.db.session
		valid_keys = ['email', 'password', 'name', 'github', 'birth_date', 'linkedin']
		try:
			validate_request(body, valid_keys)
			inviter = get_jwt_identity().get('inviter_id')
			if not inviter:
				return {'message': 'Invalid invite'}, 400 
			data = {**body, 'inviter': inviter}
			query = UserModel(**data)
			session.add(query)
			session.commit()
			return jsonify(query), 201
		except BadRequest as e:
			return jsonify(e.msg), e.status
		except IntegrityError as e:
			return {'message': 'Email already registered'}, 409
	
	@classmethod
	def login(cls):
		body = request.get_json()
		valid_keys = ['email', 'password']
		try:
			validate_request(body, valid_keys)
			query = UserModel.query.filter_by(email=body['email']).first()
			if not query:
				return {'message': 'wrong email or password'}, 403
			if query.compare_password(body['password']):
				identity={
					'id': query.id,
					'name': query.name,
					'staff_level': query.staff_level,
					'is_staff': query.staff_level > -1,
				}
				exp = datetime.timedelta(hours=24 * 7)
				return { 
					'token': create_access_token(
						identity=identity,
						expires_delta=exp )
					}, 200
			return {'message': 'wrong email or password'}, 403
		except BadRequest as e:
			return jsonify(e.msg), e.status
	
	@classmethod
	def serialize_user(cls, user):
		github_base = 'https://github.com/' 
		output = {
			'id': user.id,
			'name': user.name,
			'is_staff': user.staff_level > -1,
			'staff_level': user.staff_level,
			'github': github_base + user.github,
			'avatar': github_base + user.github + '.png',
			'linkedin': user.linkedin,
			'inviter': user.inviter
		}
		return output

	@classmethod
	def get(cls, id = None):
		if id:
			user = UserModel.query.get(id)
			if not user:
				return {'message': 'User not found.'}, 404
			return cls.serialize_user(user), 200
		else:
			user = UserModel.query.all()
			arr = []
			for u in user:
				arr.append(cls.serialize_user(u))
			return jsonify(arr), 200
				

	@classmethod
	@jwt_required()
	def delete(cls):

		session = current_app.db.session
		try:
			identity = get_jwt_identity()
			id = identity.get('id') 
			if id is None:
				return { 'error': 'Invalid Token.' }, 401
			user = UserModel.query.get(id)
			if not user:
				return {'error': 'User not found.'}, 404
			session.delete(user)
			session.commit()
			return '', 204
		except BadRequest as e:
			return jsonify(e.msg), e.status
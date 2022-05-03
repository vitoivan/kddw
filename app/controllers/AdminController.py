from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from flask import jsonify, current_app, request
from app.controllers.utils import validate_request

from app.models.user import UserModel
from app.models.errors import BadRequest
from app.assets.mail import html
from app.middlewares.is_staff import is_staff

class AdminController:

	@classmethod
	def is_more_badass(cls, user):
		staff_level = get_jwt_identity().get('staff_level')
		if user.staff_level == -1:
			return True
		return user.staff_level	> staff_level
	
	@staticmethod
	def get_invite_token(identity):
		invite_identity = {
			'inviter_id': identity.get('id')
		}
		return create_access_token(identity=invite_identity) 
			
	@classmethod
	@jwt_required()
	@is_staff
	def delete_user(cls, id: int):

		session = current_app.db.session
		try:
			user = UserModel.query.get(id)
			if not user:
				return {'error': 'User not found.'}, 404
			if not cls.is_more_badass(user):
				return { 'error': 'No enough staff level' }, 401
			session.delete(user)
			session.commit()
			return '', 204
		except BadRequest as e:
			return jsonify(e.msg), e.status

	@classmethod
	@jwt_required()
	@is_staff
	def add_staff(cls, id: int):

		session = current_app.db.session
		try:
			user = UserModel.query.get(id)
			if not user:
				return {'error': 'User not found.'}, 404
			if not cls.is_more_badass(user):
				return { 'error': 'No enough staff level' }, 401

			staff_level = get_jwt_identity().get('staff_level')
			setattr(user, 'staff_level', staff_level + 1)
			session.add(user)
			session.commit()
			return '', 200
		except BadRequest as e:
			return jsonify(e.msg), e.status
	
	@classmethod
	@jwt_required()
	@is_staff
	def remove_staff(cls, id: int):

		session = current_app.db.session
		try:
			user = UserModel.query.get(id)
			if not user:
				return {'error': 'User not found.'}, 404
			if not cls.is_more_badass(user):
				return { 'error': 'No enough staff level' }, 401

			setattr(user, 'staff_level', -1)
			session.add(user)
			session.commit()
			return '', 200
		except BadRequest as e:
			return jsonify(e.msg), e.status

	@classmethod
	def send_invite(cls, to_address):
		identity = get_jwt_identity()

		name = identity.get('name')
		if not name:
			return {'message': 'Invalid Token.'} 
		inviter_name = name.capitalize()	
		token = cls.get_invite_token(identity)	

		subject = f"{inviter_name} is inviting you to KDDW"	
		link = f'http://localhost:3333/{token}'
		body = html.replace('$name', inviter_name)
		body = body.replace('$url', link)
		current_app.sendMail(to_address, subject, body)

	@classmethod
	@jwt_required()
	@is_staff
	def create_invite(cls):

		body = request.get_json()
		try:
			validate_request(body, ['email'])
			user = UserModel.query.filter_by(email=body['email']).first()
			if user:
				return {'error': 'Email already registered'}, 409
			cls.send_invite(body['email'])
			return '', 200
		except BadRequest as e:
			return jsonify(e.msg), e.status
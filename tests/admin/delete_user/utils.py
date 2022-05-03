from tests.admin.delete_user.mocks import admin, new_user_valid, new_user_login
import json
from flask import url_for
from app.controllers.AdminController import AdminController
from flask_jwt_extended import decode_token

def login(data, client):
	res = client.post(
		url_for('user_blueprint.login'), 
        headers={'Content-Type': 'application/json'},
		data=json.dumps(data)
	)	
	client.application.db.session.rollback()
	return res.json

def register(data, client):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'Bearer ' + data['token']
	}
	data.pop('token')
	res = client.post(
		url_for('user_blueprint.register'), 
        headers=headers,
		data=json.dumps(data['user'])
	)
	client.application.db.session.rollback()
	return res

def get_invite(client):
	token = login(admin, client)['token']
	decoded = decode_token(token)['sub']
	invite = AdminController.get_invite_token(decoded)
	client.application.db.session.rollback()
	return invite 

def delete_user(data, client):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'Bearer ' + data['token'] 
	}
	res = client.delete(
		url_for('admin_blueprint.delete_user', id=data['id']), 
        headers=headers,
	)	
	client.application.db.session.rollback()
	return res

def get_user(id, client):

	url = ''.join(['/api/users/', str(id)])
	res = client.get(
		url,
        headers={
			'Content-Type': 'application/json',
			'Accept': 'application/json'
		},
	)	
	client.application.db.session.rollback()
	return res.json


def create_and_get_ordinary_user(client):

	invite = get_invite(client)
	user = register({'token': invite, 'user': new_user_valid['user']}, client).json
	token = login(new_user_login, client)['token']
	return [get_user(user['id'], client), token]	
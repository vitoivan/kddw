from tests.user.register.mocks import admin
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

def delete_user(token, client):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'Bearer ' + token 
	}
	res = client.delete(
		url_for('user_blueprint.delete'), 
        headers=headers,
	)	
	client.application.db.session.rollback()
	return res
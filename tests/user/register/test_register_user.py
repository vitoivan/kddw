from flask import url_for
from tests.user.register.utils import login, register, get_invite, delete_user
from tests.user.register.mocks import admin, new_user_valid, missing_keys

def test_register_without_invite(client):
	res =  client.post(url_for('user_blueprint.register'))
	assert res.status_code == 401 

def test_register_with_invalid_invite(client):
	data = {
		'token': login(admin, client)['token'],
		'user': new_user_valid['user']
	}
	res = register(data, client)

	assert res.json['message'] == 'Invalid invite' 
	assert res.status_code == 400

def test_register_with_invalid_user(client):
	data = {
		'token': get_invite(client),
		'user': missing_keys['user']
	}
	res = register(data, client)

	assert res.json['invalid keys'][0] == 'random_key'
	assert res.status_code == 400 

def test_register_with_valid_user(client):
	data = {
		'token': get_invite(client),
		'user': new_user_valid['user']
	}
	res = register(data, client)
	user_login = {
		'email': new_user_valid['user']['email'], 
		'password': new_user_valid['user']['password']
	}
	token = login(user_login, client)['token']
	delete_user(token, client)
	assert res.status_code == 201 
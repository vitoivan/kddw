import json
from flask import url_for

def login(data, client):
	return client.post(
		url_for('user_blueprint.login'), 
        headers={'Content-Type': 'application/json'},
		data=json.dumps(data)
	)	
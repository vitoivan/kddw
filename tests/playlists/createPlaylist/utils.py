from tests.playlists.createPlaylist.mocks import admin
import json
from flask import url_for
from app.controllers.AdminController import AdminController

def login(data, client):
	res = client.post(
		url_for('user_blueprint.login'), 
        headers={'Content-Type': 'application/json'},
		data=json.dumps(data)
	)	
	client.application.db.session.rollback()
	return res.json
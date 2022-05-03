import json
from flask import url_for
from tests.playlists.createPlaylist.mocks import admin, valid_playlist
from tests.playlists.createPlaylist.utils import login 


def test_create_playlist_with_valid_data(client):
	
	admin_token = login(admin, client)['token']
	headers = {
		'Authorization': 'Bearer ' + admin_token,
		'Content-Type': 'application/json',
	}
	res = client.post(
		url_for('playlist_blueprint.register'),
		headers=headers,
		data=json.dumps(valid_playlist)
	)		

	print(res.json)
	assert False
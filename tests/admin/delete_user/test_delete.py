from tests.admin.delete_user.utils import delete_user, login, create_and_get_ordinary_user
from tests.admin.delete_user.mocks import admin 

def test_delete_user_with_valid_token(client):
	
	adm_token = login(admin, client)['token']
	user, token = create_and_get_ordinary_user(client)
	res = delete_user({'token': adm_token, 'id': user['id']}, client)
	assert res.status_code == 204
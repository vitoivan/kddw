from tests.user.delete.utils import login, register, get_invite, delete_user
from tests.user.delete.mocks import new_user_valid 

def test_delete_user_with_invalid_token(client):
	invite = get_invite(client)	
	register({'token': invite, 'user': new_user_valid['user']}, client)
	user_login = {
		'email': new_user_valid['user']['email'], 
		'password': new_user_valid['user']['password']
	}
	user_token = login(user_login, client)['token']
	res = delete_user(invite, client)
	delete_user(user_token, client)
	assert res.status_code == 401 
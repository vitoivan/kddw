from tests.admin.addStaff.utils import delete_user, remove_staff, add_staff, login, get_user, create_and_get_ordinary_user
from tests.admin.addStaff.mocks import admin

def test_remove_staff_with_valid_id(client):
	
	adm_token = login(admin, client)['token']
	user, token = create_and_get_ordinary_user(client)
	add_staff({'token': adm_token, 'id': user['id']}, client)
	res = remove_staff({'token': adm_token, 'id': user['id']}, client)
	user = get_user(user['id'], client)
	delete_user(token, client)

	assert user['is_staff'] == False 
	assert res.status_code == 200

def test_remove_staff_with_invalid_id(client):

	adm_token = login(admin, client)['token']
	user, token = create_and_get_ordinary_user(client)
	add_staff({'token': adm_token, 'id': user['id']}, client)
	res = remove_staff({'token': adm_token, 'id': 0}, client)
	user = get_user(user['id'], client)
	delete_user(token, client)

	assert user['is_staff'] == True 
	assert res.status_code == 404 
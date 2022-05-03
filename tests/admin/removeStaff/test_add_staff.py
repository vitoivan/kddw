from tests.admin.removeStaff.utils import delete_user, add_staff, login, get_user, create_and_get_ordinary_user
from tests.admin.removeStaff.mocks import admin

def test_add_staff_with_valid_id(client):
	
	adm_token = login(admin, client)['token']
	user, token = create_and_get_ordinary_user(client)
	# Add staff to the created user using the admin token
	res = add_staff({'token': adm_token, 'id': user['id']}, client)
	# get the created user data 
	user = get_user(user['id'], client)
	# Delete the user created
	delete_user(token, client)
	assert user['is_staff'] == True 
	assert res.status_code == 200

def test_add_staff_with_invalid_id(client):

	adm_token = login(admin, client)['token']
	user, token = create_and_get_ordinary_user(client)
	# Adding staff to the wrong user using the admin token
	staff = add_staff({'token': adm_token, 'id': -1}, client)
	# get created user data
	user = get_user(user['id'], client)
	# Delete created user
	delete_user(token, client)
	assert user['is_staff'] == False
	assert staff.status_code ==  404 


def test_add_staff_with_ordinary_token(client):

	user, token = create_and_get_ordinary_user(client)
	# Adding staff to the wrong user using the admin token
	staff = add_staff({'token': token, 'id': user['id']}, client)
	# get created user data
	user = get_user(user['id'], client)
	# Delete created user
	delete_user(token, client)
	assert user['is_staff'] == False
	assert staff.status_code ==  401 
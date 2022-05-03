from tests.user.login.mocks import correct_user, incorrect_email, incorrect_pwd 
from tests.user.login.utils import login

def test_when_user_is_registered_with_right_credentials(client):

	res = login(correct_user, client) 
	status_exp = 200
	assert res.status_code == status_exp 

def test_when_user_is_registered_with_wrong_email(client):

	res = login(incorrect_email, client) 
	status_exp = 403 
	assert res.status_code == status_exp 

def test_when_user_is_registered_with_wrong_password(client):

	res = login(incorrect_pwd, client) 
	status_exp = 403 
	assert res.status_code == status_exp 
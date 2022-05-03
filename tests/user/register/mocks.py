from copy import deepcopy

admin = {
	'email': 'admin@gmail.com',
	'password': '123456'
}

new_user_valid = {
	'user': {
		'email': 'viictor.ivan@gmail.com',
		'password': '123456',
		'name': 'Victor Ivan',
		'linkedin': '',
		'github': '',
		'birth_date': '2000-12-15'
	}
}

missing_keys = deepcopy(new_user_valid) 
missing_keys['user'].pop('email')

missing_keys = deepcopy(new_user_valid) 
missing_keys['user'].update({'random_key':'random_value'})
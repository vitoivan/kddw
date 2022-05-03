from app.models.errors import BadRequest

def check_valid_keys(data, valid_keys):
	invalid_keys = []

	for k, v in data.items():
		if k not in valid_keys:
			invalid_keys.append(k)
	
	if len(invalid_keys) > 0:
		msg = {
			'error': 'Some keys are invalid',
			'valid keys': valid_keys,
			'invalid keys': invalid_keys
		}
		raise BadRequest(msg)

def check_missing_keys(data, valid_keys):
	is_valid = []
	
	for k, v in data.items():
		if k in valid_keys:
			is_valid.append(k)
	
	if len(is_valid) != len(valid_keys):
		msg = {
			'error': 'Some keys are missing',
			'missing_keys': [k for k in valid_keys if k not in is_valid]
		}
		raise BadRequest(msg)

def validate_request(data, valid_keys):
	check_missing_keys(data, valid_keys)
	check_valid_keys(data, valid_keys)
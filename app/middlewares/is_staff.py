import json
from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import Response

def is_staff(fnc):
	@wraps(fnc)
	def wrapper(*args, **kwargs):
		if not get_jwt_identity().get('is_staff'):
			return Response(json.dumps({'message': 'Unauthorized'}), 401)
		return fnc(*args, **kwargs)
	return wrapper
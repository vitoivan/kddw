from flask.blueprints import Blueprint
from app.controllers.UserController import UserController

user_bp = Blueprint('user_blueprint', __name__, url_prefix='/api')

user_bp.post('/users')(UserController.register)
user_bp.post('/users/login')(UserController.login)
user_bp.get('/users')(UserController.get)
user_bp.get('/users/<int:id>')(UserController.get)
user_bp.delete('/users')(UserController.delete)
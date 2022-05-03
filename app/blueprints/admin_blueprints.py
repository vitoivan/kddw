from flask.blueprints import Blueprint
from app.controllers.AdminController import AdminController 

admin_bp = Blueprint('admin_blueprint', __name__, url_prefix='/api')

admin_bp.delete('/admin/users/<int:id>')(AdminController.delete_user)
admin_bp.post('/admin/users/staff/add/<int:id>')(AdminController.add_staff)
admin_bp.post('/admin/users/staff/remove/<int:id>')(AdminController.remove_staff)
admin_bp.post('/admin/invite')(AdminController.create_invite)
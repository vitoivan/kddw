from flask.blueprints import Blueprint
from app.controllers.PlaylistsController import PlaylistController

playlist_bp = Blueprint('playlist_blueprint', __name__, url_prefix='/api')

playlist_bp.post('/playlists')(PlaylistController.register)
playlist_bp.delete('/playlists/<int:id>')(PlaylistController.delete)
playlist_bp.get('/playlists')(PlaylistController.get)
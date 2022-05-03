from .utils import validate_request
from flask import current_app

from app.models.videos import VideoModel
from app.models.youtube import YoutubeModel
from app.models.errors import BadRequest


class VideosController:

	@staticmethod
	def get_or_create_yt_video(yt):
		data = YoutubeModel.query.filter_by(youtube=yt).first()
		if not data:
			data = YoutubeModel(youtube=yt)
		return data
		
	@classmethod
	def register(cls, videos, session):
		all_videos = []
		try:
			for video in videos:
				validate_request(video, ['youtube', 'title', 'description'])
				youtube_id = video.pop('youtube')
				yt_obj = cls.get_or_create_yt_video(youtube_id)		
				new_video = VideoModel(**video)
				yt_obj.videos.append(new_video)
				all_videos.append(new_video)
			for video in all_videos:
				session.add(video)
			session.commit()
			return all_videos 
		except BadRequest as e:
			msg = {
				'message': 'Invalid video format',
				'expected': ['youtube', 'title', 'description']
			}
			raise BadRequest(msg) 
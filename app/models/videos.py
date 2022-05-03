from sqlalchemy import VARCHAR, Column, ForeignKey, Integer
from app.configs.database import db
from dataclasses import dataclass
from typing import Optional

@dataclass
class VideoModel(db.Model):

	__tablename__ = 'videos' 

	id: Optional[int]
	youtube_id: str
	title: str
	description: str
	
	# User data
	id = Column(Integer, primary_key=True)
	youtube_id = Column(Integer, ForeignKey('youtube.id'))
	title = Column(VARCHAR(255), nullable=False)
	description = Column(VARCHAR(255 * 2), nullable=False)
	pkaylist = Column(Integer, ForeignKey('playlists.id'))
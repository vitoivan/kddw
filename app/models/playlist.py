from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship
from app.configs.database import db
from dataclasses import dataclass, field
from typing import List, Optional

from app.models.videos import VideoModel

@dataclass
class PlaylistModel(db.Model):

	__tablename__ = 'playlists'

	id: Optional[int]
	title: str
	description: str
	owner: int
	videos: List[VideoModel] = field(default_factory=list)

	id = Column(Integer, primary_key=True)
	title = Column(VARCHAR(255), nullable=False)
	description = Column(VARCHAR(255), nullable=False)
	owner = Column(Integer, nullable=False)
	videos = relationship('VideoModel', backref='playlist')
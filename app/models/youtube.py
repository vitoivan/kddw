from sqlalchemy import Column, Integer, VARCHAR
from app.configs.database import db
from dataclasses import dataclass
from typing import Optional
from sqlalchemy.orm import relationship

@dataclass
class YoutubeModel(db.Model):

	__tablename__ = 'youtube'

	id: Optional[int]
	youtube: str
	
	# Youtube data 
	id = Column(Integer, primary_key=True)
	youtube = Column(VARCHAR(255), nullable=False)
	videos = relationship('VideoModel', backref='youtube')
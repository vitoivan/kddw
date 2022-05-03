from sqlalchemy import Column, Integer, VARCHAR, Date, ForeignKey 
from app.configs.database import db
from dataclasses import dataclass
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class UserModel(db.Model):

	__tablename__ = 'users'

	id: Optional[int]
	name: str
	github: str
	linkedin: str
	staff_level: int
	
	# User data
	id = Column(Integer, primary_key=True)
	name = Column(VARCHAR(127), nullable=False)
	email = Column(VARCHAR(255), nullable=False, unique=True)
	password_hash = Column(VARCHAR(255), nullable=False)
	birth_date = Column(Date, nullable=False)
	
	# User level
	staff_level = Column(Integer, default=-1)
	inviter = Column(Integer, nullable=False)

	# Contact
	github = Column(VARCHAR(255), nullable=False)
	linkedin = Column(VARCHAR(255), nullable=False, default='')

	@property
	def password(self):
		raise AttributeError('Password is not accessible')
	
	@password.setter
	def password(self, pwd):
		self.password_hash = UserModel.get_hash(pwd)
	
	@staticmethod
	def get_hash(pwd):
		return generate_password_hash(pwd)

	def compare_password(self, pwd):
		return check_password_hash(self.password_hash, pwd)
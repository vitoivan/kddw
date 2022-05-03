class BadRequest(Exception):

	def __init__(self, msg):
		self.msg = msg
		self.status = 400
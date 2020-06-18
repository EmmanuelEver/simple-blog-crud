from app import db
from datetime import datetime

class Blog(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(30), nullable = False )
	sub_title = db.Column(db.String(30), nullable = False)
	content = db.Column(db.Text, nullable = False)
	author = db.Column(db.String(20), nullable = False, default = 'N/A')
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

	def __init__(self, title, sub_title, content, author, date_posted):
		self.title       = title
		self.sub_title   = sub_title
		self.content     = content
		self.author    	 = author
		self.date_posted = date_posted


	def __repr__(self):
		return {"title" : self.title, "sub_title": self.sub_title, "content" : self.content, "author" : self.author, "date_posted" : self.date_posted}

	@classmethod
	def find_by_id(cls,id):
		blog_post 		  = cls.query.get(id)
		return blog_post

	
	def add_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()

	def update_from_db(self, **data):
		self.title  	= data["title"]
		self.author 	= data["author"]
		self.sub_title	= data["sub_title"]
		self.content 	= data["content"]
		db.session.commit()
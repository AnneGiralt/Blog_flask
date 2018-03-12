#from app import Post
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at= db.Column(db.DateTime)
    author = db.Column(db.String(255))
    adress = db.Column(db.String(255))
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    note = db.Column(db.Float)

def create_post(title,author, content, adress, note):
	p = Post(title = title, author = author, adress = adress, content = content, created_at = datetime.now(), note =note)
	db.session.add(p)
	db.session.commit()


if __name__ == '__main__':
	title = input('enter title : ')
	adress = input('enter adress : ')
	content = input('enter content : ')
	note = input('enter note : ')
	create_post(title = title, author = 'Anne', content = content,adress = adress, note = note)
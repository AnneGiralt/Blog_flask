from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from serializer import *



#from mocks import Post


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at= db.Column(db.DateTime)
    author = db.Column(db.String(255))
    adress = db.Column(db.String(255))
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    note = db.Column(db.Float)



def __repr__(self):
        return '<Post "{}">'.format(self.title)


@app.route('/')
def home():
	return render_template('pages/home.html')

@app.route('/about')
def about():
	return render_template('pages/about.html')

@app.route('/contact')
def contact():
	return render_template('pages/contact.html')


@app.route('/pages/blog')
def post_index():
	return render_template('posts/index.html', posts = Post.query.all())



@app.route('/blog/posts/<id>')
def detail(id):
	return render_template('posts/detail.html', post = Post.query.get(id))


@app.route('/api/getposts', methods= ['GET'])
def get_posts():
    posts =  Post.query.all()
    P = PostSchema(many=True)
    var = P.dump(posts).data

    return jsonify(var)


if __name__ == '__main__':
	app.run(debug=True)
	db.create_all()
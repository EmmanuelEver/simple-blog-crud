from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import model
app = Flask(__name__)
db  = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

@app.route('/')
def home():
	return render_template('home.html')



@app.route('/posts', methods = ['GET', 'POST'])
def posts():
	if request.method == 'POST':
		data = {
		"title" 	: request.form["title"],
		"sub_title" : request.form["sub-title"],
		"content" 	: request.form["content"],
		"author" 	: request.form["author"],
		"date_posted" : request.form.get("date_posted")
		}
		blog = model.Blog(**data)
		blog.add_to_db()
		return redirect(url_for('posts'))
	blog_posts = model.Blog.query.all()
	return render_template('posts.html', posts = blog_posts)



@app.route('/post/<int:id>')
def post(id):
	print(id)
	blog = model.Blog.find_by_id(id)
	return render_template('post.html', post = blog.__repr__())



@app.route('/posts/update/<int:id>', methods=['POST'])
def edit(id):
	data = {
		"title" : request.form["title"],
		"sub_title" : request.form["sub-title"],
		"content" : request.form["content"],
		"author" : request.form["author"]
	}
	blog = model.Blog.find_by_id(id)
	blog.update_from_db(**data)
	return redirect(url_for('posts'))



@app.route('/posts/delete/<int:id>')
def delete(id):
		blog = model.Blog.find_by_id(id)
		blog.delete_from_db()
		return redirect(url_for('posts'))




if __name__ == '__main__':
	app.run(debug=True)
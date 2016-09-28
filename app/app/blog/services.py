from app import db
from app.blog.models import BlogPost as Post

class BlogService(object):

    def delete(self, post):
        db.session.delete(post)
        db.session.commit()

    def save_update(self, post):
        db.session.add(post)
        db.session.commit()

    def get_by_slug(self, slug):
        return Post.query.filter_by(slug=slug).first()

    def get_by_title(self, title):
        return Post.query.filter_by(title=title).first()

    def get_all(self):
        return Post.query.all()

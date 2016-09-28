from flask import Blueprint, request

from flask_restful import Api, Resource
from flask_restful import abort, fields, marshal_with, reqparse

from app import db
from app.blog.models import BlogPost as Post
from app.blog.forms import CreateOrUpdateBlogForm

blog_bp = Blueprint('blog_api', __name__)
api = Api(blog_bp)

post_fields = {
    'id': fields.Integer,
    'created': fields.DateTime,
    'modified': fields.DateTime,
    'title': fields.String,
    'content': fields.String,
    'slug': fields.String,
    'published': fields.Boolean
}

list_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'slug': fields.String,
}

class BlogPostDetail(Resource):

    @marshal_with(post_fields)
    def get(self, slug):
        post = Post.query.filter_by(slug=slug).first()

        if not post:
            abort(404, error="Post {} doesn't exist".format(slug))

        return post

    def delete(self, slug):
        post = Post.query.filter_by(slug=slug).first()

        if not post:
            abort(404, error="Post {} doesn't exist".format(slug))

        #TODO wrap this into a service
        db.session.delete(post)
        db.session.commit()
        #TODO wrap this into a service

        return {}, 204

    @marshal_with(post_fields)
    def put(self, slug):
        post = Post.query.filter_by(slug=slug).first()

        if not post:
            abort(404, error="Post {} doesn't exist".format(slug))

        form = CreateOrUpdateBlogForm(data=request.get_json(force=True))

        #TODO wrap this into a service
        form.populate_obj(post)
        db.session.add(post)
        db.session.commit()
        #TODO wrap this into a service

        return post, 200


class BlogPostList(Resource):

    @marshal_with(list_fields)
    def get(self):
        post = Post.query.all()
        return post

    @marshal_with(post_fields)
    def post(self):
        form = CreateOrUpdateBlogForm(data=request.get_json(force=True))

        if not form.validate():
            abort(400, errors=form.errors)

        #TODO wrap this into a service
        post = Post(title=form.title.data, content=form.content.data)
        existing_post = Post.query.filter_by(title=post.title).first()

        if existing_post:
            abort(409, error="Post {} already exist".format(post.title))

        db.session.add(post)
        db.session.commit()
        #TODO wrap this into a service

        return post, 201

api.add_resource(BlogPostDetail, '/<string:slug>')
api.add_resource(BlogPostList, '/')

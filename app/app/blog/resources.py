from flask import Blueprint, request

from flask_restful import Api, Resource
from flask_restful import abort, fields, marshal_with, reqparse

from app.blog.models import BlogPost as Post
from app.blog.forms import CreateOrUpdateBlogForm
from app.blog.services import BlogService

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
    service = BlogService()

    @marshal_with(post_fields)
    def get(self, slug):
        post = self.service.get_by_slug(slug)

        if not post:
            abort(404, error="Post {} doesn't exist".format(slug))

        return post

    def delete(self, slug):
        post = self.service.get_by_slug(slug)

        if not post:
            abort(404, error="Post {} doesn't exist".format(slug))

        self.service.delete(post)

        return {}, 204

    @marshal_with(post_fields)
    def put(self, slug):
        post = self.service.get_by_slug(slug)

        if not post:
            abort(404, error="Post {} doesn't exist".format(slug))

        form = CreateOrUpdateBlogForm(data=request.get_json(force=True))

        if not form.validate():
            abort(400, errors=form.errors)

        form.populate_obj(post)
        self.service.save_update(post)

        return post, 200


class BlogPostList(Resource):
    service = BlogService()

    @marshal_with(list_fields)
    def get(self):
        return self.service.get_all()

    @marshal_with(post_fields)
    def post(self):
        form = CreateOrUpdateBlogForm(data=request.get_json(force=True))

        if not form.validate():
            abort(400, errors=form.errors)

        post = Post(title=form.title.data, content=form.content.data)

        existing_post = self.service.get_by_title(post.title)
        if existing_post:
            abort(409, error="Post {} already exist".format(post.title))

        self.service.save_update(post)

        return post, 201

api.add_resource(BlogPostDetail, '/<string:slug>')
api.add_resource(BlogPostList, '/')

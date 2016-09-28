from flask import Blueprint, request

from flask_restful import Api, Resource
from flask_restful import abort, fields, marshal_with, marshal, reqparse

from app import db
from app.pages.models import Page
from app.pages.forms import CreateOrUpdatePageForm

page_bp = Blueprint('page_api', __name__)
api = Api(page_bp)

page_fields = {
    'id': fields.Integer,
    'created': fields.DateTime,
    'modified': fields.DateTime,
    'title': fields.String,
    'content': fields.String,
    'slug': fields.String,
}

list_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'slug': fields.String,
}

class PageDetail(Resource):

    @marshal_with(page_fields)
    def get(self, slug):
        page = Page.query.filter_by(slug=slug).first()

        if not page:
            abort(404, error="Page {} doesn't exist".format(slug))

        return page

    def delete(self, slug):
        page = Page.query.filter_by(slug=slug).first()

        if not page:
            abort(404, error="Page {} doesn't exist".format(slug))

        #TODO wrap this into a service
        db.session.delete(page)
        db.session.commit()
        #TODO wrap this into a service

        return {}, 204

    @marshal_with(page_fields)
    def put(self, slug):
        page = Page.query.filter_by(slug=slug).first()

        if not page:
            abort(404, error="Page {} doesn't exist".format(slug))

        form = CreateOrUpdatePageForm(data=request.get_json(force=True))

        if not form.validate():
            abort(400, errors=form.errors)

        #TODO wrap this into a service
        form.populate_obj(page)
        db.session.add(page)
        db.session.commit()
        #TODO wrap this into a service

        return page, 200


class PageList(Resource):

    # TODO: Use pagination
    @marshal_with(list_fields)
    def get(self):
        pages = Page.query.all()
        return pages

    @marshal_with(page_fields)
    def post(self):
        form = CreateOrUpdatePageForm(data=request.get_json(force=True))

        if not form.validate():
            abort(400, errors=form.errors)

        #TODO wrap this into a service
        page = Page(title=form.title.data, content=form.content.data)
        existing_page = Page.query.filter_by(title=page.title).first()

        if existing_page:
            abort(409, error="Page {} already exist".format(page.title))

        db.session.add(page)
        db.session.commit()
        #TODO wrap this into a service

        return page, 201

api.add_resource(PageDetail, '/<string:slug>')
api.add_resource(PageList, '/')

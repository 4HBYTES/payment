from flask import Blueprint, request

from flask_restful import Api, Resource
from flask_restful import abort, fields, marshal_with, marshal, reqparse

from app.pages.models import Page
from app.pages.services import PageService
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

    service = PageService()

    @marshal_with(page_fields)
    def get(self, slug):
        page = self.service.get_by_slug(slug)

        if not page:
            abort(404, error="Page {} doesn't exist".format(slug))

        return page

    def delete(self, slug):
        page = self.service.get_by_slug(slug)

        if not page:
            abort(404, error="Page {} doesn't exist".format(slug))

        self.service.delete(page)

        return {}, 204

    @marshal_with(page_fields)
    def put(self, slug):
        page = self.service.get_by_slug(slug)

        if not page:
            abort(404, error="Page {} doesn't exist".format(slug))

        form = CreateOrUpdatePageForm(data=request.get_json(force=True))

        if not form.validate():
            abort(400, errors=form.errors)

        form.populate_obj(page)
        self.service.save_update(page)

        return page, 200


class PageList(Resource):

    service = PageService()

    # TODO: Use pagination
    @marshal_with(list_fields)
    def get(self):
        return self.service.get_all()

    @marshal_with(page_fields)
    def post(self):
        form = CreateOrUpdatePageForm(data=request.get_json(force=True))

        if not form.validate():
            abort(400, errors=form.errors)

        page = Page(title=form.title.data, content=form.content.data)
        existing_page = self.service.get_by_title(page.title)

        if existing_page:
            abort(409, error="Page {} already exist".format(page.title))

        self.service.save_update(page)

        return page, 201

api.add_resource(PageDetail, '/<string:slug>')
api.add_resource(PageList, '/')

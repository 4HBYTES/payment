from app import db
from app.pages.models import Page

class PageService(object):

    def delete(self, page):
        db.session.delete(page)
        db.session.commit()

    def save_update(self, page):
        db.session.add(page)
        db.session.commit()

    def get_by_slug(self, slug):
        return Page.query.filter_by(slug=slug).first()

    def get_by_title(self, title):
        return Page.query.filter_by(title=title).first()

    def get_all(self):
        return Page.query.all()

from mock import Mock
from datetime import datetime

from app.pages.models import Page

class MockPageService(object):

    def _make_mock(self, id=1):
        page = Mock(spec=Page)
        page.id = id
        page.title = "Page #{}".format(id)
        page.content = "Page number {}".format(id)
        page.slug = "page-{}".format(id)
        page.created = datetime.now()
        page.modified = datetime.now()

        return page

    def delete(self, page):
        pass

    def save_update(self, page):
        pass

    def get_by_slug(self, slug):
        return self._make_mock()

    def get_failure_by_slug(self, slug):
        return None

    def get_by_title(self, title):
        return self._make_mock()

    def get_failure_by_title(self, title):
        return None

    def get_all(self):
        return [
            self._make_mock(1),
            self._make_mock(2)
        ]

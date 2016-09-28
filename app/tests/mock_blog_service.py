from mock import Mock
from datetime import datetime

from app.blog.models import BlogPost

class MockBlogService(object):

    def _make_mock(self, id=1):
        post = Mock(spec=BlogPost)
        post.id = id
        post.title = "Post #{}".format(id)
        post.content = "Post number {}".format(id)
        post.slug = "post-{}".format(id)
        post.created = datetime.now()
        post.modified = datetime.now()

        return post

    def delete(self, post):
        pass

    def save_update(self, post):
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

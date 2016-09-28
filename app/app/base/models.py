import re
from unicodedata import normalize
from datetime import datetime

from app import db

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.now())
    modified = db.Column(
        db.DateTime,
        default=datetime.now(),
        onupdate=datetime.now()
    )

    def set_slug(self, text):
        slug = self.slugify(text)
        self.slug = slug

    @staticmethod
    def slugify(text, delim=u'-'):
        _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
        text = unicode(text)
        """Generates an slightly worse ASCII-only slug."""
        result = []
        for word in _punct_re.split(text.lower()):
            word = normalize('NFKD', word).encode('ascii', 'ignore')
            if word:
                result.append(word)
        return unicode(delim.join(result))

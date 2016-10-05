from flask import request
from logging import Formatter, StreamHandler, Filter
from uuid import uuid4
import json
import os


class ContextualFilter(Filter):
    levelnames = dict(
        DEBUG=0,
        INFO=1,
        WARNING=2,
        ERROR=3,
        CRITICAL=4
    )

    def _get_request_body(self):
        if request.form:
            return request.form.keys()[0]
        return {}

    def _map_headers(self, item):
        return item

    def filter(self, log_record):
        log_record.host = request.url_root
        log_record.uri = request.path
        log_record.method = request.method
        log_record.remote_host = request.environ.get('REMOTE_ADDR')
        log_record.remote_port = request.environ.get('REMOTE_PORT')
        log_record.body = self._get_request_body()
        log_record.request_id = uuid4()
        log_record.headers = json.dumps({k: self._map_headers(v) for k, v in request.headers.iteritems()})
        log_record.level = self.levelnames[log_record.levelname]
        log_record.app_id = os.environ.get('APP_ID')
        log_record.instance_id = os.environ.get('INSTANCE_ID')
        log_record.instance_type = os.environ.get('INSTANCE_TYPE')
        log_record.instance_number = os.environ.get('INSTANCE_NUMBER')
        log_record.commit_id = os.environ.get('COMMIT_ID')

        return True

handler = StreamHandler()
handler.setFormatter(Formatter('''
{
    "timestamp": "%(asctime)s",
    "status_code": 500,
    "message": "%(message)s",
    "host": "%(host)s",
    "remote_host": "%(remote_host)s",
    "remote_port": %(remote_port)d,
    "uri": "%(uri)s",
    "level": %(level)d,
    "headers": %(headers)s,
    "body": %(body)s,
    "method": "%(method)s",
    "request_id": "%(request_id)s",
    "app_id": "",
    "instance_id": "",
    "instance_type": "",
    "instance_number": "",
    "commit_id": ""
}
'''))

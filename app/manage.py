#!/usr/bin/env python
from flask_script import Manager, Server

from auth import app

manager = Manager(app)
manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()

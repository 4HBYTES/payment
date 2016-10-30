#!/usr/bin/env python
from app import app
from flask_script import Manager, Server

manager = Manager(app)
manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()

#!/usr/bin/env python
from app import app
from flask_script import Manager, Server
from flask_migrate import MigrateCommand

manager = Manager(app)
manager.add_command('runserver', Server())
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

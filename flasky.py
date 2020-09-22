# -*- coding:utf-8 -*-
import os
from app import creat_app, db
from flask_migrate import Migrate, MigrateCommand
from app.models import Info
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap


app = creat_app(os.getenv('FLASK_CONFIG') or 'development')
migrate = Migrate(app, db)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Info=Info)


manager.add_command("shell", Shell(make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    app.run()

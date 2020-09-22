# -*- coding:utf-8 -*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_cors import CORS

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()


def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app, origins="*", supports_credentials=True)

    moment.init_app(app)
    db.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

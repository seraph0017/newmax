#!/usr/bin/env python
#encoding:utf-8
import yaml
import os

from flask import Flask
from ext import db, mail, cache


def create_app():
    conf = get_config()
    app = Flask(__name__)
    app.config.update(conf['ENV'][os.getenv('ENV')])
    db.init_app(app)
    mail.init_app(app)
    cache.init_app(app,config=conf['CACHE_CONFIG'])
    return app


def get_config():
    with open('config.yml','rb') as f:
        config_file = f.read()
    conf = yaml.load(config_file)
    return conf



app = create_app()

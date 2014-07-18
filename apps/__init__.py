#!/usr/bin/env python
#encoding:utf-8
from flask import Flask
from ext import db, mail, cache

app = Flask(__name__)
db.init_app(app)
mail.init_app(app)
cache.init_app(app)

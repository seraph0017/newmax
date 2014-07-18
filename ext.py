#!/usr/bin/env python
#encoding:utf-8
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache


db = SQLAlchemy()
cache = Cache()
mail = Mail()

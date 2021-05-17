# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os

from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_pyfile('settings.py')
bootstrap = Bootstrap(app)

from frontend import views
# from sayhello.static.file import errors

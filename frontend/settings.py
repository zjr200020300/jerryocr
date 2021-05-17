# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os

from frontend import app

UPLOAD_FOLDER = os.path.join(app.static_folder, 'origin')
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

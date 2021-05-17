# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from natsort import natsorted

from flask import flash, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename

from frontend import app
import os

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file_filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_filename))

    all_origin_files = os.listdir(os.path.join(app.static_folder, 'origin'))
    origin_images = [file_name for file_name in all_origin_files if file_name.endswith('.png')]
    natsorted(origin_images)
    all_result_files = os.listdir(os.path.join(app.static_folder, 'result'))
    result_images = [file_name for file_name in all_result_files if file_name.endswith('.png')]
    natsorted(result_images)
    result_text_file = open(os.path.join(app.static_folder, 'text', 'images.txt'))
    result_text = result_text_file.read()
    return render_template('index.html', origin_images=origin_images, result_images=result_images,
                           result_text=result_text)


@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files[]' not in request.files:
        flash('No file part')
        return 'error'
    file = request.files['files[]']
    if file.filename == '':
        flash('No selected file')
        return 'error'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'OK'

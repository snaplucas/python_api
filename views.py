# coding: utf-8
import os
from werkzeug import secure_filename
from flask import request, current_app, send_from_directory, render_template

from db import noticias
from news_app import app


@app.route("/noticias/cadastro", methods=["GET", "POST"])
def cadastro():
    ...
    return render_template('cadastro.html', title=u"Inserir nova noticia")


@app.route("/")
def index():
    ...
    return render_template('index.html', ...)


@app.route("/noticia/<int:noticia_id>")
def noticia(noticia_id):
    ...
    return render_template('noticia.html', noticia=noticia)


@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)

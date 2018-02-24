# -*- coding: utf-8 -*-

from flask import Flask
from flask import redirect, abort
import json
from flask import make_response
from flask import jsonify


app = Flask('python_api')


@app.route("/")
def hello_world():
    return "Hello World! <strong>I am learning Flask</strong>", 200


@app.route("/<name>")
def index(name):
    if name.lower() == "lucas":
        return "Olá {}".format(name), 200
    else:
        return "Not Found", 404


@app.route("/html_page/<nome>")
def html_page(nome):
    return u"""
    <html>
       <head><title>Ainda não sei usar o Jinja2 :)</title></head>
       <body>
          <h1>Olá %s Coisas que você não deve fazer.</h1>
          <ul>
            <li> Escrever html direto na view </li>
            <li> Tentar automatizar a escrita de html via Python</li>
            <li> deixar de usar o Jinja2 </li>
          </ul>
       </body>
    </html>
    """ % nome


@app.route("/json_api")
def json_api():
    pessoas = [{"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]
    return jsonify(pessoas=pessoas, total=len(pessoas))


app.run(debug=True, use_reloader=True)

# -*- coding: utf-8 -*-

from bottle import route, run, template, SimpleTemplate, static_file

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/opt/ts/bootstrap')

@route('/')
def index():
    return template('index')

run(host='localhost', port=8080)

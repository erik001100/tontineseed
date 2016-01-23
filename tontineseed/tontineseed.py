# -*- coding: utf-8 -*-

from bottle import route, run, template, SimpleTemplate, static_file

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/tmp/bootstrap-3.3.6-dist')

@route('/')
def index():
    return template('index')

run(host='localhost', port=8080)

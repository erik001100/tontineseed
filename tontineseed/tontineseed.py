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

@route('/pricefile/<filehash>')
def pricing(filehash):
    # use an api to get torrent total size
    # use an api to get torrent hash
    filehash = 'cd8158937344b2a066446bed7e7a0c45214f1245'
    return template('pricing', filehash=filehash)

@route('/upload')
def upload():
    return template('upload')

run(host='localhost', port=8080)

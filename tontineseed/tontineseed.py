# -*- coding: utf-8 -*-
import pdb
import os
import hashlib
from bottle import route, run, template, SimpleTemplate, static_file, request, redirect
#from TransmissionClient import NoSuchTorrent, TransmissionClient

# FILE UPLOAD FROM STACK OVERFLOW
# http://stackoverflow.com/questions/22839474/python-bottle-how-to-upload-media-files-without-dosing-the-server

MAX_SIZE = 10 * 1024 * 1024 # 10MB
BUF_SIZE = 8192

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/opt/ts/bootstrap')

@route('/')
def index():
    return template('index')

@route('/upload', method='POST')
def upload():
    '''Upload function from StackOverflow'''
    
    # Move to config file
    upload_dir = '/tmp/torrents/'

    #hash file being uploaded
    h = hashlib.new('sha1')

    files = request.files
    print files, type(files)
    data = request.files.data

    if(data is not None):
        fileinfo = {}
        uploadfile = data
        #pdb.set_trace()
        print uploadfile.filename, type(uploadfile)
        fileinfo['name'] = uploadfile.filename
        target_path = os.path.join(upload_dir, uploadfile.filename)
        print target_path

        # add Ron.Rothman's code
        # hash file as being read
        data_blocks = []
        buf = uploadfile.file.read(8192)
        h.update(buf)
        while buf:
            data_blocks.append(buf)
            buf = uploadfile.file.read(8192)
            h.update(buf)

        fileinfo['hash'] = h.hexdigest()
        my_file_data = ''.join(data_blocks)

        with open(target_path, 'wb') as tf:
            tf.write(my_file_data)
            fileinfo['size'] = tf.tell()

        # write data to server db
        # write filename, hash, size, generated address for payment, datetime, calculateprice

    redirect('/pricefile/{0}'.format(fileinfo['hash']))
    return None

@route('/sendtorrent', method='GET')
def upload_form():
    return template('upload_form')

@route('/pricefile/<filehash>')
def pricing(filehash):
    # get info from db to display here
    # generate qr code for address

    return template('pricing', filehash=filehash)


run(host='localhost', port=8080)

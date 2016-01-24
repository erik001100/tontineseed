# -*- coding: utf-8 -*-
import pdb
from bottle import route, run, template, SimpleTemplate, static_file, request

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
    #upload_dir = get_upload_dir_path()
    upload_dir = '/tmp/torrents/'

    files = request.files
    ##files = request.files.get('files')
    # add this line

    data = request.files.data
    ##data = request.files.data.get('data')

    pdb.set_trace()
    print files, type(files)

    if(files is not None):
        file = files.file
        print file.filename, type(file)
        target_path = get_next_file_name(os.path.join(upload_dir, file.filename))
        print target_path

        # add Ron.Rothman's code
        data_blocks = []
        buf = data.file.read(8192)
        while buf:
            data_blocks.append(buf)
            buf = data.file.read(8192)

        my_file_data = ''.join(data_blocks)
        # do something with the file data, like write it to target
        file(target_path,'wb').write(my_file_data)

    return None

@route('/sendtorrent', method='GET')
def upload_form():
    return template('upload_form')

@route('/pricefile/<filehash>')
def pricing(filehash):
    # use an api to get torrent total size
    # use an api to get torrent hash
    filehash = 'cd8158937344b2a066446bed7e7a0c45214f1245'
    return template('pricing', filehash=filehash)

run(host='localhost', port=8080)

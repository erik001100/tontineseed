===============================
tontineseed
===============================

.. image:: https://img.shields.io/pypi/v/tontineseed.svg
        :target: https://pypi.python.org/pypi/tontineseed

.. image:: https://img.shields.io/travis/erik998/tontineseed.svg
        :target: https://travis-ci.org/erik998/tontineseed

.. image:: https://readthedocs.org/projects/tontineseed/badge/?version=latest
        :target: https://readthedocs.org/projects/tontineseed/?badge=latest
        :alt: Documentation Status


seed your torrents using a tontine as incentive

* Free software: MIT license
* Documentation: https://tontineseed.readthedocs.org.

TODO
----

* Fix installation instructions
* Setup page to upload torrents
* Setup pricing function for torrent size
* Extract hierarchically deterministic Bitcoin address for uploader to send payment to
* Show page with bitcoin address and price to uploader
* On payment received, show list of torrent pools
* etc, much more...

BRANCHES
--------
* master - Plain html mostly. Interaction should be possible via CURL.
* js - Interaction via Javascript and Dropzone

DEVELOPER HINTS
---------------
* `Uploading Files With DropZone JS and Express JS`_

Features
--------

* TODO

Instructions
------------

* `Setup Python and Virtual Environment`_.
* Create a virtual environement. In your Projects directory, on command line run "mkvirtualenv tontineseed"
* clone this repo
* change directory to repo, run this in the command line "pip install -r requirements.txt"
* change directory to repo, run this in command line "ln -s assets/bootstrap/ /tmp/bootstrap"
* to run server, change directory to tontineseed/tontineseed and run "python tontineseed.py"



Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Setup Python and Virtual Environment`: http://thinkingnotes.net/setting-up-python.html
.. _`Uploading Files With DropZone JS and Express JS`: http://thejackalofjavascript.com/uploading-files-with-dropzone-js-and-express-js/

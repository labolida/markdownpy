# Markdown easy served as HTML

 Open source
 Python3 + Flask + Markdown

## Easy installation

After "download" or "git clone" this project, do:


    $ python3 -m venv venv
    $ pip install -r requirements.txt

    On windows, use: python -m venv venv

    If markdown library can't be found when you are starting the server, try:

        $ rm -r ./venv
        $ python -m venv venv
        $ pip install markdown
        $ pip install flask

## Start the server

    $ source ./venv/bin/activate
    $ flask --debug run --host 0.0.0.0 --port 80 --reload

    On windows, use: venv\Scripts\activate.bat

    Remember, on linux you must to use "sudo" to bind on low ports. 
    You could use --port 5000 instead.

## Access the url with a browser:

    http://127.0.0.1:5009
    http://127.0.0.1
    http://127.0.0.1/api/
    http://127.0.0.1/view/
    http://127.0.0.1/raw/filename.png

## Docker Container

 https://hub.docker.com/repository/docker/lmldocker/markdownpy/general

    docker run -it --rm -p 8080:8080 lmldocker/markdownpy:1.0

 or

    docker run -d -p 8080:8080 \
    -v /area6/docker/volume/markdownpy/data:/area6/python/dev/markdownpy/data \
    -v /area6/docker/volume/markdownpy/resources:/area6/python/dev/markdownpy/resources \
    lmldocker/markdownpy:1.0

 The server runs on --reload mode!

# Authors

    Leonardo M Labolida (Spain/Brasil)
    Tomás R Pita        (Spain/Venezuela)

# Donation

<script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script>
<script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#29abe0', 'V7V0LUYPW');kofiwidget2.draw();</script> 

<a href='https://ko-fi.com/V7V0LUYPW' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

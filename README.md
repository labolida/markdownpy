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


# Authors
    Leonardo M Labolida (Spain/Brasil)
    Tomás R Pita        (Spain/Venezuela)

# Donation

    Soon via paypal

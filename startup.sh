#!/bin/sh
echo " "
echo " "
echo MarkdownPy WebServer Starting...
source ./venv/bin/activate
flask run --host 0.0.0.0 --port 8888 --reload

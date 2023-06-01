##########################################################################################
###  MARKDOWNPY EASY WEB SERVER - Keep It Simple, Stupid!
##########################################################################################

from flask import Flask
from flask import send_file
import markdown
import os

app = Flask(__name__)

##########################################################################################
# CONFIG

#DATA_PATH = "/disk01/repositories/markdownpy-data/"
DATA_PATH = r'C:\\area\\dev\\markdownpy\\data\\'
RESOURCES_PATH = 'C:\\area\\dev\\markdownpy\\resources\\'

##########################################################################################
@app.route('/')
def root():
    res = []
    for path in os.listdir(DATA_PATH):
        if os.path.isfile(os.path.join(DATA_PATH, path)):
            res.append(path)
    print(res)
    html=""
    for fn in res:
        html = html + "<a href='/view/"+ fn + "'>" + fn + "</a><br>";
    return html

##########################################################################################
@app.route('/api')
def api():
    res = []
    for path in os.listdir(DATA_PATH):
        if os.path.isfile(os.path.join(DATA_PATH, path)):
            res.append(path)
    print(res)
    return res

##########################################################################################
@app.route('/view' , methods=["GET", "POST"] )
@app.route('/view/' , methods=["GET", "POST"] )
@app.route('/view/<filename>' , methods=["GET", "POST"] )
def view( filename="index.md"):
    html = ""
    html = html + fileRead( RESOURCES_PATH+"header.html")
    markdown_content = fileRead( DATA_PATH+filename)
    html = html + markdown.markdown(markdown_content)
    html = html + fileRead( RESOURCES_PATH+"footer.html")
    print("\n\n----------------------------------------------------\n\n")
    print(html)
    return html

##########################################################################################
@app.route('/raw' , methods=["GET"] )
@app.route('/raw/<filename>' , methods=["GET"] )
def raw (filename=None):
    print("RAWFILES")
    return send_file( DATA_PATH+filename )

##########################################################################################
def fileRead( filename ):
    with open( filename, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    return text

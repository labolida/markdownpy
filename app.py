##########################################################################################
###  MARKDOWN EASY SERVER
##########################################################################################

from flask import Flask
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
    return res


##########################################################################################
@app.route('/view')
def view():
    html = ""
    html = html + fileRead( RESOURCES_PATH+"header.html")
    markdown_content = fileRead( DATA_PATH+"index.md")
    html = html + markdown.markdown(markdown_content)
    html = html + fileRead( RESOURCES_PATH+"footer.html")
    print("\n\n----------------------------------------------------\n\n")
    print(html)
    return html



##########################################################################################
def fileRead( filename ):
    with open( filename, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    return text


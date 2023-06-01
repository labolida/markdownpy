##########################################################################################
###  MARKDOWN EASY SERVER
##########################################################################################

from flask import Flask
import markdown
import os

app = Flask(__name__)

##########################################################################################
# CONFIG

DATA_PATH = r'C:\\area\\dev\\markdownpy\\data\\'

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
    with open( DATA_PATH+"index.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    print("\n\n\n\n\n----------------------------------------------------\n\n\n\n")
    print(html)
    html = "<html> css include " + html
    return html





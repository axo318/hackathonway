# Imports
import os

# Web imports
from flask import Flask, render_template, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename

# Begin Serving
app = Flask(__name__)


## ROUTES ##

# Index
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    Renders the initial page with the options for actions on the website.
    :return: initial html page
    """
    return render_template('index.html')


### MAIN ###
if __name__=='__main__':
    app.run(host='0.0.0.0', port=PORT)
    print('[main]: main(): Server is listening on port:', PORT)

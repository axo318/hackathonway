# Imports
import os

# Custom imports
from lib.controller import Controller

# Web imports
from flask import Flask, render_template, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename

PORT = 5000

# Begin Serving
app = Flask(__name__)
controller = Controller()
controller.run()


## ROUTES ##

# Index
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    Renders the initial page with the options for actions on the website.
    :return: initial html page
    """

    '''
    DEBUG
    '''
    reply = controller.dealWithRequest('login','van')
    print(reply)
    return render_template('index.html')


### MAIN ###
if __name__=='__main__':
    app.run(host='0.0.0.0', port=PORT)
    print('[main]: main(): Server is listening on port:', PORT)

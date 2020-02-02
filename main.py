# Imports
import os

# Custom imports
from lib.controller import Controller

# Web imports
from flask import Flask, render_template, flash, request, redirect, url_for, session

PORT = 5000

# Begin Serving
app = Flask(__name__)

# Begin Back-End
controller = Controller()


'''
ROUTES
'''
# Index
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', message='FER')

@app.route('/fill_ticket', methods=['GET', 'POST'])
def fill_ticket():
    return render_template('fill_ticket.html')

@app.route('/submit_ticket', methods=['GET', 'POST'])
def submit_ticket():
    name = request.form['name']
    if len(name)>0:
        # Deal with Ticket
        controller.dealWithRequest('ticket', data=request.form)
        return render_template('index.html', message='SUCCESS')
    else:
        return render_template('index.html', message='ERROR, PLEASE RETRY')

@app.route('/doctor_dashboard', methods=['GET', 'POST'])
def doctor_dashboard():
    return render_template('doctor_dashboard.html')

@app.route('/next_patient', methods=['GET', 'POST'])
def next_patient():
    # Do smth
    return redirect(url_for('doctor_dashboard'))



### MAIN ###
if __name__=='__main__':
    app.run(host='0.0.0.0', port=PORT)
    print('[main]: main(): Server is listening on port:', PORT)

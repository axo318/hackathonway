# Imports
import os

# Custom imports
from lib.controller import Controller
from lib.database import *
# Web imports
from flask import Flask, render_template, flash, request, redirect, url_for, session

# GLOBALSs
PORT = 5000
DOCTOR_RESPONSE_GEORGE = 'George Smith'
DOCTOR_RESPONSE_LISA = 'Lisa Anna'
DOCTOR_RESPONSE_JOHNNY = 'Johnny Smith'
DOCTOR_RESPONSE_MIA = 'Mia Khalifa'

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

@app.route('/close_ticket', methods=['GET', 'POST'])
def close_ticket():
    docid = request.form['doctorname']
    patname = request.form['name']
    hit = 0
    if len(patname)>0:
        # Deal with Ticket
        tickets = getTickets()
        for x in tickets:
            if x.get_username() == patname:
                diagnosis = x.get_diagnosis()
                hit += 1
                break
        if hit==0:
            return render_template('doctor_dashboard.html', message='Patient name not found.')
        if request.form['diag']==diagnosis:
            return render_template('index.html', message='SUCCESS')
        else:
            return render_template('doctor_dashboard.html', message='Please call for assistance. Diagnosis deemed invalid.')
    else:
        return render_template('index.html', message='ERROR, PLEASE RETRY')

@app.route('/doctor_dashboard', methods=['GET', 'POST'])
def doctor_dashboard():
    return render_template('doctor_dashboard.html')

@app.route('/next_patient', methods=['GET', 'POST'])
def next_patient():
    # response is the name of the doctor
    response = request.args.get('doc')
    controller.dealWithRequest('next_patient', data=response)
    # CALL

    # Get name of doctor
    # move queue
    return redirect(url_for('doctor_dashboard'))



### MAIN ###
if __name__=='__main__':
    app.run(host='0.0.0.0', port=PORT)
    print('[main]: main(): Server is listening on port:', PORT)

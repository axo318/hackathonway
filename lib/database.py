'''
File contains functions used for dealing with databases
'''
import pandas as pd
from .config import *
from .Classes.ticket import Ticket
# from .Controller import Controller
from .Classes.person import Patient
from .Classes.person import Doctor

# GLOBALS
TABLE_ID_DOCTORS  = 0
TABLE_ID_PATIENTS = 1
TABLE_ID_TICKETS  = 2


# Authentication
# 0-doctor; 1-patient; 2-ticket
def authenticate(username,password): #-> bool
    df = getTable(TABLE_ID_PATIENTS)
    rows = df[(df[LOGIN_USERNAME_COL]==username) & (df[LOGIN_PASSWORD_COL]==password)].shape[0]
    if (rows != 1):
        return False
    else:
        return True

#-----------------------------------------------------------
# Getters
#-----------------------------------------------------------

# returns list of Tickets
def getTickets(): #-> list[Ticket]
    df = getTable(TABLE_ID_TICKETS)
    listTickets = []
    for i in range(df.shape[0]):
        row = df.iloc[i]
        id          = row.iloc[0]
        username    = row.iloc[1]
        symptoms    = row.iloc[2].split(";")
        diagnosis   = row.iloc[3]
        doctor      = row.iloc[4]
        speciality  = row.iloc[5]
        listTickets.append(Ticket(id=id,username=username,\
            symptoms=symptoms,diagnosis=diagnosis,doctor=doctor,\
            speciality=speciality))
    return listTickets

# returns list of Doctors
def getDoctors(): #-> list[Doctor]
    df = getTable(TABLE_ID_DOCTORS)
    # print(df)
    listDoctors = []
    for i in range(df.shape[0]):
        row = df.iloc[i]
        # print('row: {}'.format(row))
        name        = row.iloc[0]
        speciality  = row.iloc[1]
        rating      = row.iloc[2]
        temp_doc = Doctor(name=name, speciality=speciality, rating=rating)
        # print('temp_doc: {}'.format(temp_doc))
        listDoctors.append(temp_doc)
    return listDoctors

# returns list of Patients
def getPatients(): #-> list[Patient]
    df = getTable(TABLE_ID_PATIENTS)
    listPatients = []
    for i in range(df.shape[0]):
        row = df.iloc[i]
        username    = row.iloc[0]
        password    = row.iloc[1]
        dob         = row.iloc[2]
        listPatients.append(Patient(username=username,password=password,dob=dob))
    return listPatients

#-----------------------------------------------------------
# Adders
#-----------------------------------------------------------

# add new Doctor to existing csv file
def addDoctor(doctor): #-> bool
    # get Doctor attributes
    doctor_name_given      = doctor.get_name()
    print('doctor given:\n{}\n'.format(doctor))
    # check if already in lsit of Doctors
    if(checkIfPresent(TABLE_ID_DOCTORS,doctor_name_given)):
        #remove Doctor from list of doctors
        removeData(TABLE_ID_DOCTORS,doctor_name_given)
    # add Doctor to list of Doctors
    df_doctors = getTable(TABLE_ID_DOCTORS)
    print('BEFORE ADDING NEW\nshould print all doctors now...')
    print('df_doctors\n{}'.format(df_doctors))
    attributes_doctor = [doctor.get_name(),doctor.get_speciality(),doctor.get_rating()]
    print('attributes_doctor={}'.format(attributes_doctor))
    df_doctors.loc[len(df_doctors),:] = attributes_doctor
    print(df_doctors)
    # print('AFTER ADDING NEW\nshould print all doctors now...')
    saveTable(TABLE_ID_DOCTORS,df_doctors)
    return True

# add patient to existing csv file
def addPatient(patient): #-> bool
    # get Doctor attributes
    patient_username_given = patient.get_username()
    # check if already in lsit of Doctors
    if(checkIfPresent(TABLE_ID_PATIENTS,patient_username_given)):
        #remove Doctor from list of doctors
        removeData(TABLE_ID_PATIENTS,patient_username_given)
    # add Doctor to list of Doctors
    df_patients = getTable(TABLE_ID_PATIENTS)
    attributes_patient = [patient.get_username(),patient.get_password(),patient.get_dob()]
    df_patients.loc[len(df_patients),:] = attributes_patient
    saveTable(TABLE_ID_PATIENTS,df_patients)
    return True

# add new ticket to existing csv file
def addTicket(ticket): #-> bool
    # get Doctor attributes
    ticket_id_given = ticket.get_id()
    # check if already in lsit of Doctors
    if(checkIfPresent(TABLE_ID_TICKETS,ticket_id_given)):
        #remove Doctor from list of doctors
        removeData(TABLE_ID_TICKETS,ticket_id_given)
    # add Doctor to list of Doctors
    df_tickets = getTable(TABLE_ID_TICKETS)
    temp_id =ticket.get_id()
    temp_username =ticket.get_username()
    temp_symptoms_str = ticket.get_symptoms()
    temp_diagnosis =ticket.get_diagnosis()
    temp_doctor =ticket.get_doctor().get_name()
    temp_speciality =ticket.get_speciality()
    attributes_ticket = [temp_id,temp_username,temp_symptoms_str,temp_diagnosis,temp_doctor,temp_speciality]
    df_tickets.loc[df_tickets.shape[0]] = attributes_ticket
    saveTable(TABLE_ID_TICKETS,df_tickets)
    print(df_tickets.to_string())
    return True

#-----------------------------------------------------------
# Removals
#-----------------------------------------------------------
def removeData(table_id,identifier):
    print('removing data from table')
    if(table_id==TABLE_ID_DOCTORS):
        # get existing one
        df_doctors     = getTable(TABLE_ID_DOCTORS)
        # remove undesired
        df_doctors_new = df_doctors[df_doctors[DOCTORS_NAME_COL]!=identifier]
        # overwrite csv file
        saveTable(TABLE_ID_DOCTORS,df_doctors_new)
        return True
    if(table_id==TABLE_ID_PATIENTS):
        df_patients     = getTable(TABLE_ID_PATIENTS)
        df_patients_new = df_patients[df_patients[LOGIN_USERNAME_COL]!=identifier]
        saveTable(TABLE_ID_PATIENTS,df_patients_new)
        return True
    if(table_id==TABLE_ID_TICKETS):
        df_tickets     = getTable(TABLE_ID_TICKETS)
        df_tickets_new = df_tickets[df_tickets[TICKETS_ID_COL]!=identifier]
        saveTable(TABLE_ID_TICKETS,df_tickets_new)
        return True
    else:
        return False
#-----------------------------------------------------------------
# HELPER METHODS
#-----------------------------------------------------------------

# retuers pandas object
# 0-doctor; 1-patient; 2-ticket
def getTable(table_id):
    if(table_id==TABLE_ID_DOCTORS):
        return pd.read_csv(DATA_DOCTORS)
    if(table_id==TABLE_ID_PATIENTS):
        return pd.read_csv(DATA_LOGIN)
    if(table_id==TABLE_ID_TICKETS):
        return pd.read_csv(DATA_TICKETS)
    else:
        return -1

# overwrite existing csv file
# 0-doctor; 1-patient; 2-ticket
def saveTable(table_id,df):
    if(table_id==TABLE_ID_DOCTORS):
        df.to_csv(DATA_DOCTORS,index=False)
        return True
    if(table_id==TABLE_ID_PATIENTS):
        df.to_csv(DATA_LOGIN,index=False)
        return True
    if(table_id==TABLE_ID_TICKETS):
        df.to_csv(DATA_TICKETS,index=False)
        return True
    else:
        return False

# 0-doctor; 1-patient; 2-ticket
def checkIfPresent(table_id,identifier):
    if(table_id==TABLE_ID_DOCTORS):
        print('check if doctor in list\nidentifier={}'.format(identifier))
        df = getTable(TABLE_ID_DOCTORS)
        rows = df[df[DOCTORS_NAME_COL]==identifier].shape[0]
        print(rows)
        if (rows == 0):
            print('returns false')
            return False
        else:
            print('returns true')
            return True
    if(table_id==TABLE_ID_PATIENTS):
        df = getTable(TABLE_ID_PATIENTS)
        rows = df[df[LOGIN_USERNAME_COL]==identifier].shape[0]
        if (rows == 0):
            return False
        else:
            print('returns true')
            return True
    if(table_id==TABLE_ID_TICKETS):
        df = getTable(TABLE_ID_TICKETS)
        print('df[df[TICKETS_ID_COL]]={}'.format(df[df[TICKETS_ID_COL] == identifier]))
        rows = df[df[TICKETS_ID_COL]==identifier].shape[0]
        if (rows == 0):
            return False
        else:
            print('returns true')
            return True

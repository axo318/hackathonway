'''
File contains functions used for dealing with databases
'''
import pandas as pd
from .config import *

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
    listDoctors = []
    for i in range(df.shape[0]):
        row = df.iloc[i]
        name        = row.iloc[0]
        speciality  = row.iloc[1]
        listDoctors.append(Doctor(name=name,speciality=speciality))
    return listDoctors

# returns list of Patients
def getPatients(): #-> list[Patient]
    df = getTable(TABLE_ID_TICKETS)
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
    # check if already in lsit of Doctors
    if(checkIfPresent(TABLE_ID_DOCTORS,doctor_name_given)):
        #remove Doctor from list of doctors
        removeData(TABLE_ID_DOCTORS,doctor_name_given)
    # add Doctor to list of Doctors
    df_doctors = getTable(TABLE_ID_DOCTORS)
    attributes_doctor = [doctor.get_name(),doctor.get_specialty()]
    df_doctors.loc[df_doctors.shape[0]] = attributes_doctor
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
    df_patients.loc[df_patients.shape[0]] = attributes_patient
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
    attributes_ticket = [ticket.get_id(),ticket.get_username(),ticket.get_symptoms(),ticket.get_diagnosis(),ticket.get_doctor(),ticket.get_speciality()]
    df_tickets.loc[df_tickets.shape[0]] = attributes_ticket
    saveTable(TABLE_ID_TICKETS,df_patients)
    return True

#-----------------------------------------------------------
# Removals
#-----------------------------------------------------------
def removeData(table_id,identifier):
    if(table_id==0):
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
    if(table_id==0):
        return pd.read_csv(DATA_DOCTORS)
    if(table_id==1):
        return pd.read_csv(DATA_LOGIN)
    if(table_id==2):
        return pd.read_csv(DATA_TICKETS)
    else:
        return -1

# overwrite existing csv file
# 0-doctor; 1-patient; 2-ticket
def saveTable(table_id,df):
    if(table_id==TABLE_ID_DOCTORS):
        df.to_csv(DATA_DOCTORS)
        return True
    if(table_id==TABLE_ID_PATIENTS):
        df.to_csv(DATA_LOGIN)
        return True
    if(table_id==TABLE_ID_TICKETS):
        df.to_csv(DATA_TICKETS)
        return True
    else:
        return False

# 0-doctor; 1-patient; 2-ticket
def checkIfPresent(table_id,identifier):
    if(table_id==TABLE_ID_DOCTORS):
        df = getTable(TABLE_ID_DOCTORS)
        rows = df[df[DOCTORS_NAME_COL]==identifier].shape[0]
        if (rows != 0):
            return True
    if(table_id==TABLE_ID_PATIENTS):
        df = getTable(TABLE_ID_PATIENTS)
        rows = df[df[LOGIN_USERNAME_COL]==identifier].shape[0]
        if (rows != 0):
            return True
    if(table_id==TABLE_ID_TICKETS):
        df = getTable(TABLE_ID_TICKETS)
        rows = df[df[TICKETS_ID_COL]==identifier].shape[0]
        if (rows != 0):
            return True
    else:
        return False

import os
import pandas as pd

# DIR_LIB = '/'.join(os.path.realpath(__file__).split('/')[:-1])
DIR_LIB = os.path.dirname(os.path.realpath(__file__))
DIR_ROOT = os.path.join(DIR_LIB,'..')
DIR_DATA = os.path.join(DIR_ROOT,'data')
DIR_DISEASE_DATA = os.path.join(DIR_DATA, "diseasesdata")

DATA_DOCTORS = os.path.join(DIR_DATA,'data_doctors.csv')
DATA_LOGIN   = os.path.join(DIR_DATA,'data_login.csv')
DATA_TICKETS = os.path.join(DIR_DATA,'data_tickets.csv')

dis_ids = pd.read_csv(os.path.join(DIR_DISEASE_DATA,'diagnosisNamenId.csv'))
symp_ids = pd.read_csv(os.path.join(DIR_DISEASE_DATA,'symptomsNids.csv'))
syms_dis_weights = pd.read_csv(os.path.join(DIR_DISEASE_DATA,'symptomsDiseasesNWeight.csv'))
diagnosis_amount_df = pd.read_csv(os.path.join(DIR_DISEASE_DATA,"symptomsExtraInfo.csv"))

REQUEST_DICTIONARY = os.path.join(DIR_DATA,'request_dictionary.csv')
IDENTIFIER_COLUMN_NAME = 'Identifier'
CLASSNAME_COLUMN_NAME = 'ClassName'

#login dataset headers
LOGIN_USERNAME_COL = 'username'
LOGIN_PASSWORD_COL = 'password'
LOGIN_DOB_COL = 'dob'
# doctors dataset headers
DOCTORS_NAME_COL = 'name'
DOCTORS_SPECIALITY_COL = 'speciality'
DOCTORS_RATING_COL = 'rating'
# tickets dataeset headers
TICKETS_ID_COL = 'id'
TICKETS_USERNAME_COL = 'username'
TICKETS_SYMPTOMS_COL = 'symptoms'
TICKETS_DIAGNOSIS_COL = 'diagnosis'
TICKETS_DOCTOR_COL = 'doctor'
TICKETS_SPECIALTY_COL = 'speciality'

# requests headers
IDENTIFIER_COLUMN_NAME = 'Identifier'
CLASSNAME_COLUMN_NAME = 'ClassName'

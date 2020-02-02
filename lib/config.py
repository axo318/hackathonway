import os

# DIR_LIB = '/'.join(os.path.realpath(__file__).split('/')[:-1])
DIR_LIB = os.path.dirname(os.path.realpath(__file__))
DIR_ROOT = os.path.join(DIR_LIB,'..')
DIR_DATA = os.path.join(DIR_ROOT,'data')

DATA_DOCTORS = os.path.join(DIR_DATA,'data_doctors.csv')
DATA_LOGIN   = os.path.join(DIR_DATA,'data_login.csv')
DATA_TICKETS = os.path.join(DIR_DATA,'data_tickets.csv')

REQUEST_DICTIONARY = os.path.join(DIR_DATA,'request_dictionary.csv')

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

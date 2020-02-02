# This class is for person

class Patient:

    def __init__(self, username=None, password=None, dob=None):
        self.USERNAME = username
        self.PASSWORD = password
        self.DOB = dob

    # -- Getters --
    def get_username(self):
        return self.USERNAME

    def get_password(self):
        return self.PASSWORD

    def get_dob(self):
        return self.DOB
    
    def __str__(self):
        str_out = 'self.USERNAME = {}\nself.PASSWORD = {}\nself.DOB = {}\n'.format(self.USERNAME,self.PASSWORD,self.DOB)
        return str_out


class Doctor:
    def __init__(self, name=None, speciality=None, rating=None):
        self.NAME = name
        self.SPECIALITY = speciality
        self.RATING = rating

    # -- Getters --
    def get_name(self):
        return self.NAME

    def get_rating(self):
        return self.RATING

    def get_speciality(self):
        return self.SPECIALITY

    def __str__(self):
        str_out = 'self.NAME = {}\nself.SPECIALITY = {}\nself.RATING={}'.format(self.NAME,self.SPECIALITY,self.RATING)
        return str_out
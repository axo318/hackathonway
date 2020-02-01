# This class is for person

class Patient:

    def __init__(self, username=None, password=None, dob=None):
        self.USERNAME = username
        self.PASSWORD = password
        self.DOB = dob

    # -- Getters --
    def get_name(self):
        return self.USERNAME

    def get_password(self):
        return self.PASSWORD

    def get_date_of_birth(self):
        return self.DOB


class Doctor:

    def __init__(self, name=None, specialty=None, rating=None):
        self.NAME = name
        self.SPECIALITY = specialty
        self.RATING = rating

    # -- Getters --
    def get_name(self):
        return self.NAME

    def get_rating(self):
        return self.RATING

    def get_speciality(self):
        return self.SPECIALITY

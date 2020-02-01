# This class is for person

class Person(object):


    # Variables
    #
    # name: (string) name of person
    # Dob: (Date) date of birth of the person
    # post code: (string) post code, address
    # ticket: (Ticket) ticket given to the person to see a doctor

    def __init__(self, name, DoB, post_code):
        self._initialise_variables(name, DoB, post_code)

    def _initialise_variables(self, name, DoB, post_code):
        self.NAME = name
        self.DoB = DoB
        self.POST_CODE = post_code
        self.TICKET = None

    def add_ticket(self, ticket):
        self.TICKET = ticket

    # -- Getters --
    def get_name(self):
        return self.NAME

    def get_date_of_birth(self):
        return self.DoB

    def get_post_code(self):
        return self.POST_CODE

    def get_ticket(self):
        return self.TICKET
    # -- Getters --    

class Patient(Person):

    def __init__(self):
        super().__init__()


class Doctor(Person):

    # Variables
    #
    # rating: (double) 0 -> 100%, never seen a patient = -100% 
    # specialties: (set) list of strings 

    def __init__(self, name, DoB, post_code, rating, specialties):
        super().__init__(name, DoB, post_code)
        self.RATING = rating
        self.SPECIALTIES = specialties

    # Gets the rating of the doctor from the database
    def get_rating_from_database(self, database):
        return None

    # -- Getters --
    def get_rating(self):
        return self.RATING

    def get_specialties(self):
        return self.SPECIALTIES
    # -- Getters --
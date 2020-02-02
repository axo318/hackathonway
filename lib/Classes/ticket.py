class Ticket(object):

    def __init__(self, id=None, username=None, symptoms=None, diagnosis=None, doctor=None, speciality=None, severity=None):
        self.ID = id
        self.USERNAME = username
        self.SYMPTOMS = symptoms
        self.DIAGNOSIS = diagnosis
        self.DOCTOR = doctor
        self.SPECIALITY = speciality
        # ----------------------
        self.SEVERITY = severity

    def close(self):
        # update model and database
        return

    # -- Update/add variables --
    def set_diagnosis(self, diagnosis):
        self.DIAGNOSIS = diagnosis

    def set_speciality(self, speciality):
        self.SPECIALITY = speciality

    def set_symptoms(self, symptoms):
        self.SYMPTOMS = self.SYMPTOMS
    # -- Update/add variables --

    # -- Getters --
    def get_id(self):
        return self.ID

    def get_username(self):
        return self.USERNAME

    def get_symptoms(self):
        return self.SYMPTOMS

    def get_diagnosis(self):
        return self.DIAGNOSIS

    def get_doctor(self):
        return self.DOCTOR

    def get_speciality(self):
        return self.SPECIALITY

    def get_queue(self):
        return self.QUEUE

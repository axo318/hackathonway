class Ticket(object):

    # Variables
    #
    # patient: (Patient) the patient
    # doctor: (Doctor) the doctor assigned to patient
    # symptoms: (Set) Set of Symptom
    # specialist: (SpecialDoctor) special doctor if needed
    # diagnosis: (Diagnosis) the diagnosis given by the doctor



    def __init__(self, patient, doctor, symptoms, queue, id):
        self._initialise_variables(patient, doctor, symptoms, queue,id)

    def _initialise_variables(self, patient, doctor, symptoms, queue, id):
        self.PATIENT = patient
        self.DOCTOR = doctor
        self.SYMPTOMS = symptoms
        self.QUEUE = queue
        self.ID = id
        # ----------------------
        self.SPECIALIST = None
        self.DIAGNOSIS = None
       
    
    def close(self):
        # update model and database 
        return

    # -- Update/add variables --
    def update_diagnosis(self, diagnosis):
        self.DIAGNOSIS = diagnosis

    def add_specialist(self, specialist):
        self.SPECIALIST = specialist

    def add_symptoms(self, symptoms):
        self.symptoms = self.symptoms
    # -- Update/add variables --

    # -- Getters --
    def get_patient(self):
        return self.PATIENT

    def get_doctor(self):
        return self.DOCTOR

    def get_symptoms(self):
        return self.SYMPTOMS

    def get_queue(self):
        return self.QUEUE

    def get_specialist(self):
        return self.SPECIALIST

    def get_diagnosis(self):
        return self.DIAGNOSIS
    # -- Getters --

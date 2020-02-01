class Diagnosis(object):

    # Variables
    #
    # id: (int) unique id for this diagnosis from the database
    # name: (string) unique name obtained from databse
    # severity: (int) ordered from 0 -> 3, the worst is 3

    def __init__(self, id, name, severity):
        self._initialise_variables(id, name, severity)

    def _initialise_variables(self, id, name, severity):
        self.ID = id
        self.NAME = name
        self.SEVERITY = severity


    # -- Getters --
    def get_name(self):
        return self.NAME

    def get_id(self):
        return self.ID

    def get_severity(self):
        return self.SEVERITY
    # -- Getters --
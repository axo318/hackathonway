class Symptom(object):

    # Variables
    #
    # id: (int) id associated with symptom
    # name: (string) name of this symptom

    def __init__(self, id, name):
        self._initialise_variables(id,name) 

    def _initialise_variables(self, id, name):
        self.ID = id
        self.NAME = name

    # -- Getters --
    def get_name(self):
        return self.NAME

    def get_id(self):
        return self.ID
    # -- Getters --
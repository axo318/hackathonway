import sys
from .Classes.ticket import Ticket
from .database import *
import string
import random

'''
Superclass for all requests
'''
class WebRequest:
    def deal(self, controller, data):
        pass

'''
Static class which returns proper request object
'''
class RequestBuilder:
    @staticmethod
    def getRequest(identifier, dict):
        class_name = dict.get(identifier)
        class_ = getattr(sys.modules[__name__], class_name)
        return class_()


'''
Request Subclasses
'''
class TicketRequest(WebRequest):
    def deal(self, controller, data):
        # Get name and symptoms
        name = data['name']
        symptoms = [data['s'+str(i)] for i in range(1,7) if len(data['s'+str(i)])>0]

        # Get unique id
        char_set = string.ascii_uppercase + string.digits
        id = ''.join(random.sample(char_set*6, 6))#'12'
        # Go to db and get number of tickets stored
        # Go to active queue anf get num of TicketRequest
        # Sum them + 1 assign to id

        # Get possible diagnosis
        diagnosis = controller.model.get_similarity(symptoms)
        severity = diagnosis.iloc[diagnosis.shape[0]-1]['Weight']
        diagnosis = diagnosis.iloc[diagnosis.shape[0]-1]['Diagnosis']

        # Make ticket
        ticket = Ticket(id=id, username=name, symptoms=symptoms, diagnosis=diagnosis, severity=severity)
        controller.addActiveTicket(ticket)

        return 'login request REPLY'
'''
gets the next patient once button is pressed
'''
class NextPatientRequest(WebRequest):
    def deal(self, controller, data):
        response = data
        # pop the last ticket from live que
        all_doctors = getDoctors()
        for doc in all_doctors:
            doc_name = doc.get_name()
            if (doc_name==response):
                controller.freeDoctors.append(doc)
                break
        # add doctor name to ticket
        # EXTRA
        # save that ticket into memory
        if(len(controller.activeQueue)>0):
            next_ticket = controller.popActiveTicket()
            next_ticket.set_doctor(doc_name)
            # !!! ADD DIAGNISOS ???
            addTicket(next_ticket)
            #

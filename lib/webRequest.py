import sys
from .classes.ticket import Ticket

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
        id = 12

        # Get possible diagnosis
        diagnosis = controller.classifier.predict(symptoms)
        severity = getSeverity(diagnosis)

        # Make ticket
        ticket = Ticket(id=id, name=name, symptoms=symptoms, diagnosis=diagnosis, severity=severity)
        controller.addActiveTicket(ticket)

        return 'login request REPLY'

import os
import pandas as pd
# Custom Imports
from .webRequest import RequestBuilder
from .config import REQUEST_DICTIONARY, IDENTIFIER_COLUMN_NAME, CLASSNAME_COLUMN_NAME
from .database import *

'''
Main class that handles requests from front-end and replies with any needed info
'''
class Controller:
    # Constructor
    def __init__(self):
        self.request_dictionary = self.readDictionary()
        self.activeQueue = []
        self.freeDoctors = []
        self.initializeVariables()

    def initializeVariables(self):
        self.freeDoctors = getDoctors()

    # Reads the csv file with available requests and returns it as dict
    def readDictionary(self):
        df = pd.read_csv(REQUEST_DICTIONARY, index_col=IDENTIFIER_COLUMN_NAME)
        d = df.to_dict().get(CLASSNAME_COLUMN_NAME)
        return d

    # Controller deals with incoming web request
    def dealWithRequest(self, classifier, data=None):
        request = RequestBuilder.getRequest(classifier, self.request_dictionary)
        reply = request.deal(self, data)
        return reply

    # Add ticket to correct place of activeQueue
    def addActiveTicket(self, ticket):
        # Check if doctors free
        if(len(self.freeDoctors)>0):
            # add & remove immediatly from the live que
            self.activeQueue.append(ticket)
            self.popActiveTicket()

        # If not add ticket to active queue
        ind = 0
        for temp_ticket in self.activeQueue:
            if temp_ticket.severity < ticket.severity:
                ind += 1
            else:
                break
        self.activeQueue.insert(ind, ticket)

    def popActiveTicket(self):
        ticket = self.activeQueue.pop()
        ticket.set_doctor(self.freeDoctors.pop(0))
        # !!! DIAGNOSIS ???
        addTicket(ticket)
        return ticket

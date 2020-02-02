import os
import pandas as pd
# Custom Imports
from .webRequest import RequestBuilder
from config import DIR_DATA, IDENTIFIER_COLUMN_NAME, CLASSNAME_COLUMN_NAME

'''
Main class that handles requests from front-end and replies with any needed info
'''
class Controller:
    # Constructor
    def __init__(self):
        self.request_dictionary = self.readDictionary()

    def run(self):
        pass

    # Reads the csv file with available requests and returns it as dict
    def readDictionary(self):
        df = pd.read_csv(DIR_DATA, index_col=IDENTIFIER_COLUMN_NAME)
        d = df.to_dict().get(CLASSNAME_COLUMN_NAME)
        '''
        DEBUGG
        '''
        print(d)
        return d

    # Controller deals with incoming web request
    def dealWithRequest(self, classifier, data):
        request = RequestBuilder.getRequest(classifier, self.request_dictionary)
        reply = request.deal(data)
        return reply

import os
import pandas as pd

# Custom Imports
from .webRequest import RequestBuilder

# Gets path of directory current file is in
path = '/'.join(os.path.realpath(__file__).split('/')[:-1])
REQ_DICT_NAME = path + '/../data/request_dictionary.csv'
IDENTIFIER_COLUMN_NAME = 'Identifier'
CLASSNAME_COLUMN_NAME = 'ClassName'

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
        df = pd.read_csv(REQ_DICT_NAME, index_col=IDENTIFIER_COLUMN_NAME)
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

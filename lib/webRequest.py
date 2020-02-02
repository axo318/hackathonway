import sys

'''
Superclass for all requests
'''
class WebRequest:
    def deal(self, data):
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
class LoginRequest(WebRequest):
    def deal(self, data):
        return 'login request REPLY'

class LogoutRequest(WebRequest):
    def deal(self, data):
        return 'logout request REPLY'

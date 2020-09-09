import random
import string
class Credentials:
    '''
    Class that generates new instance of the account credentials, with the account details to the application
    '''
    account_info = []
    def __init__ (self, account, username, password):
        self.account = account
        self.username = username
        self.password = password

        '''
        __init__ method that helps to define properties for our objects
        '''

    
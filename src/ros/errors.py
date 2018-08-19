"""
ROS Code Errors File
This file contains all the code required for declaring errors
"""

# Regular Error and code to inherit

class BaseError(object):
 
    def __init__(self, message):
 
        Exception.__init__(message)
 
        self.when = datetime.now()

# Exception Conversion Error


class ConversionError(BaseError):
    pass


# Exception Wrong Input


class WrongInput(BaseError):
    pass


# Exception Unexpected Error


class UnexpectedError(BaseError):
    pass

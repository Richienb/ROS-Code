"""
ROS Code Errors File
This file contains all the code required for declaring errors
"""
class BaseError(object):
 def __init__(self,message):
  Exception.__init__(message)
  self.when=datetime.now()
class ConversionError(BaseError):
 pass
class WrongInput(BaseError):
 pass
class UnexpectedError(BaseError):
 pass
# Created by pyminifier (https://github.com/liftoff/pyminifier)

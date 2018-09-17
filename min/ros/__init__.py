name="ros"
global __ros_stored__
__ros_stored__=None
if __debug__:
 import logging
 logging.basicConfig(level=30,filename="ros.log")
if __name__=="__main__":
 import platform
 import sys
 from.import*
 VER="ROS Code 2.0 | Running on {} {} | Python Version {}.{}.{}".format(platform.system(),platform.release(),list(sys.version_info)[0],list(sys.version_info)[1],list(sys.version_info)[2])
 print(VER)
 while True:
  if sys.version_info>(3,0):
   exec("print("+input(">> ")+")")
  else:
   exec("print("+raw_input(">> ")+")")
# Created by pyminifier (https://github.com/liftoff/pyminifier)

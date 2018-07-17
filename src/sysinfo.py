import platform
import sys

print("ROS Code 2.0 | Running on {} {} | Python Version {}.{}.{}".format(platform.system(), platform.release(), list(sys.version_info)[0], list(sys.version_info)[1], list(sys.version_info)[2]))

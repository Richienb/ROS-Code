name = "ros"

# Ensure ROS Code storage variables are global
__ros_stored__ = None
global __ros_stored__

# Activate logging if debug mode enabled
if __debug__:
    import logging
    logging.basicConfig(level=30, filename="ros.log")

# Interactive shell if launched directly
if __name__ == "__main__":
    import platform
    import sys
    from . import *
    VER = "ROS Code 2.0 | Running on {} {} | Python Version {}.{}.{}".format(
        platform.system(), platform.release(),
        list(sys.version_info)[0],
        list(sys.version_info)[1],
        list(sys.version_info)[2])
    print(VER)
    while True:
        exec("print(" + input(">> ") + ")")

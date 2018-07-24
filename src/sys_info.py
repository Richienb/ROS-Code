# Backwards Compatibility
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import str
from future import standard_library
standard_library.install_aliases()
# System Modules
import platform
import sys
# String Modules
from pprint import pprint

# Set VER (version) variable
VER = "ROS Code 2.0 | Running on {} {} | Python Version {}.{}.{}".format(
    platform.system(), platform.release(),
    list(sys.version_info)[0],
    list(sys.version_info)[1],
    list(sys.version_info)[2])

# Set VAR (variable) variable
VAR = [
    str(platform.system()),
    str(platform.release()),
    str(sys.version_info),
    str(list(sys.version_info)[0]),
    str(list(sys.version_info)[1]),
    str(list(sys.version_info)[2])
]

# Print VER


def print_ver():
    print(VER)


# Return VER


def get_ver():
    return VER


# Print VAR


def print_var():
    print(VAR)


# Return VAR


def get_var():
    return VAR


# Pretty Print VAR


def pprint_var():
    pprint(VAR)


# Detect direct execution and print ver
if __name__ == "__main__":
    print_ver()

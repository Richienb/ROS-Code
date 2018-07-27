from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import str
from future import standard_library
standard_library.install_aliases()
import platform
import sys
from pprint import pprint
VER = "ROS Code 2.0 | Running on {} {} | Python Version {}.{}.{}".format(
    platform.system(), platform.release(), list(
        sys.version_info)[0], list(
            sys.version_info)[1], list(
                sys.version_info)[2])
VAR = [str(platform.system()),
       str(platform.release()),
       str(sys.version_info),
       str(list(sys.version_info)[0]),
       str(list(sys.version_info)[1]),
       str(list(sys.version_info)[2])]


def print_ver():
    print(VER)


def get_ver():
    return VER


def print_var():
    print(VAR)


def get_var():
    return VAR


def pprint_var():
    pprint(VAR)


if __name__ == "__main__":
    print_ver()
# Created by pyminifier (https://github.com/liftoff/pyminifier)

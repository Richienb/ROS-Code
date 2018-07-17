from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import platform
import sys

print(
    "ROS Code 2.0 | Running on {} {} | Python Version {}.{}.{}".format(
        platform.system(), platform.release(), list(
            sys.version_info)[0], list(
                sys.version_info)[1], list(
                    sys.version_info)[2]))

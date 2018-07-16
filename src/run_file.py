"""
Encodes and runs a ROS Code file
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
# Main Modules
from builtins import open
from builtins import str
from sys import argv as args
from sys import exit as exitexc
import ros
import importlib
import os.path
# Initialise Backwards Compatibility
from future import standard_library
standard_library.install_aliases()

# Check if file provided in execution arguments
try:

    # Try to evalute the second execution argument (file name)
    args[1]

# Check for a evaluation error (file name not specified)
except IndexError:

    # Throw error
    print("ERROR: No ROS Code file provided in execution arguments")

    # Stop execution
    exitexc(1)


if not os.path.isfile(args[1]):
    print("ERROR: " + args[1] + " is not found.")
    exitexc(1)
    
f = open(args[1], "r")

with open(args[1]) as f:
    IGNORELINE = False
    CONTENT = f.readlines()
    CONTENT = [x.strip() for x in CONTENT if x.strip()]
    for value in enumerate(CONTENT):
        if not(value[1].startswith('!')) and IGNORELINE is False:
            if value[1].startswith('mod'):
                try:
                    importlib.import_module(
                        "ros." + value[1].split(" ")[1])
                    break
                except ModuleNotFoundError:
                    raise ImportError("Error: Unable to import")
                    exitexc(1)
            elif value[1].startswith('ext'):
                if os.path.isfile(value[1].split(" ")[1] + ".ros"):
                    pass # TODO: Allow importing of external packages
            elif value[1].startswith('imp'):
                if os.path.isfile(value[1].split(" ")[1] + ".py"):
                    importlib.import_module(value[1].split(" ")[1])
            parta = value
            firstpart = value[1].split(".")[0]
            lenoffirstpart = len(value[1].split(".")[0])
            afterpart = str(value[1][lenoffirstpart + 1:])
            apwithcomma = afterpart.replace(".", "', '")
            preprint = str(firstpart + "(" + apwithcomma + ")")
            printtext = preprint.replace("(", "('")
            lastprinttext = printtext.replace(")", "')")
            try:
                exec(str(lastprinttext))
            except Exception as exc:
                template = "ERROR: An error of type {0} occured while running line {1} because {2}"
                message = template.format(
                    type(exc).__name__, str(value[0] + 1), str(exc.args[0]))
                print(message)
                exitexc(1)
        elif value[1].startswith('!!!'):
            IGNORELINE = not IGNORELINE

exitexc(0)

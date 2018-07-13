"""
Encodes and runs a line of ROS Code
"""
# Main Modules
from sys import argv as args
from sys import exit as exitexc
import syntax
# Initialise Backwards Compatibility
from future import standard_library
standard_library.install_aliases()

try:
    args[1]
except IndexError:
    print("ERROR: No ROS Code file provided in execution arguments")
    print('Ensure the execution code looks something like this: \
    python run-file.py message_print("Hello World")')

with open(args[1]) as f:
    IGNORELINE = False
    CONTENT = args[1]
    if not(value[1].startswith('!')) and IGNORELINE is False:
        FIRSTPART = value[1].split(".")[0]
        LENOFFIRSTPART = len(value[1].split(".")[0])
        AFTERPART = str(value[1][LENOFFIRSTPART + 1:])
        APWITHCOMMA = AFTERPART.replace(".", "', '")
        PREPRINT = str(FIRSTPART + "(" + APWITHCOMMA + ")")
        PRINTTEXT = PREPRINT.replace("(", "('")
        LASTPRINTTEXT = PRINTTEXT.replace(")", "')")
        try:
            exec(str("syntax." + LASTPRINTTEXT))
        except Exception as E:
            template = "ERROR: An error of type {0} occured while running line {1} because {2}"
            message = template.format(
                type(e).__name__, str(value[0] + 1), str(E.args[0]))
            print(message)
            exitexc(1)
    elif value[1].startswith('!!!'):
        IGNORELINE = not IGNORELINE

exitexc(0)

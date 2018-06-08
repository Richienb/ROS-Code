from sys import argv as args
from sys import exit as quit
import syntax

try:
    args[1]
except IndexError:
    print("ERROR: No ROS Code file provided in execution arguments")
    print('Ensure the execution code looks something like this: python run-file.py message_print("Hello World")')

with open(args[1]) as f:
    content = args[1]
    print(content[0])
    if not(content[0] == "!") and ignoreline == False:
        firstpart = content.split(".")[0]
        lenoffirstpart = len(content.split(".")[0])
        afterpart = str(content[lenoffirstpart + 1:])
        apwithcomma = afterpart.replace(".", "', '")
        preprint = str(firstpart + "(" + apwithcomma + ")")
        printtext = preprint.replace("(", "('")
        lastprinttext = printtext.replace(")", "')")
        try:
            exec(str("syntax." + lastprinttext))
        except Exception as e:
            template = "ERROR: An error of type {0} occured because {1}"
            message = template.format(
                type(e).__name__, str(e.args[0]))
            print(message)
            quit(1)
quit(0)

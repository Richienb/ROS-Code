from sys import argv as args
from sys import exit as quit
import syntax

try:
    args[1]
except IndexError:
    print("ERROR: No ROS Code file provided in execution arguments")
    print("Ensure the execution code looks something like this: python run-file.py test.ros")

with open(args[1]) as f:
    ignoreline = False
    content = f.readlines()
    content = [x.strip() for x in content]
    for value in enumerate(content):
        if not(value[1][0] == "!") and ignoreline == False:
            firstpart = value[1].split(".")[0]
            lenoffirstpart = len(value[1].split(".")[0])
            afterpart = str(value[1][lenoffirstpart + 1:])
            apwithcomma = afterpart.replace(".", "', '")
            preprint = str(firstpart + "(" + apwithcomma + ")")
            printtext = preprint.replace("(", "('")
            lastprinttext = printtext.replace(")", "')")
            try:
                exec(str("syntax." + lastprinttext))
            except Exception as e:
                template = "ERROR: An error of type {0} occured while running line {1} because {2}"
                message = template.format(
                    type(e).__name__, str(value[0] + 1), str(e.args[0]))
                print(message)
                quit(1)
        elif content[value[0]][0] == "!!!":
            ignoreline = not(ignoreline)

quit(0)

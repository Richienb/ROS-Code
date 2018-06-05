from sys import argv as args
import syntax

with open(args[1]) as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    for value in range(len(content)):
        if len(content[value].split(" ")) > 1 and not(content[value][0] == "!"):
            firstpart = content[value].split(".")[0]
            lenoffirstpart = len(content[value].split(".")[0])
            afterpart = str(content[value][lenoffirstpart + 1:])
            apwithcomma = afterpart.replace(".", "', '")
            preprint = str(firstpart + "(" + apwithcomma + ")")
            printtext = preprint.replace("(", "('")
            lastprinttext = printtext.replace(")", "')")
            try:
                exec(str("syntax." + lastprinttext))
            except Exception as e:
                print(e.args)
                buildstring = ''
                for value in range(len(list(e.args))):
                    buildstring += (list(e.args)[value] + " ")
                print("ERROR: A problem occured while running line " + str(value) + " because of " + str(e.args[0]) + " Error Information: " + buildstring)
            print(lastprinttext)
            #exec(lastprinttext)
        #elif len(content.split(".")) == 1:
        #    raise RuntimeError('No Parameters For ' + content[value].split(" ")[0] + ' Provided!')

print("Hello, World")

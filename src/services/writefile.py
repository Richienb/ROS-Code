from compilefile import compilefile

def writefile(sourcefile, destinationfile):
    with open(destinationfile, "a") as myfile:
        for line_to_add in enumerate(compilefile(sourcefile)):
            myfile.write(line_to_add[1])

# Import custom errors module
from errors import CompilationError


def compilefile(filename):

    # Get all lines of a file and put it in a list
    filelines = open(str(filename)).read().splitlines()

    compiledlist = []

    # Compile the python command for each line in the list
    for i in enumerate(filelines):

        try:

            # If line empty
            if i[1] in ["", None]:

                # Append an empty line
                compiledlist.append("")

            # If line starts with "!"
            elif i[1][0]("!"):

                # Change the first character from "!" to "#"
                i[1] = i[1].replace("!", "#", 1)

                # Append the changed string
                compiledlist.append(i[1])

                # Skip to next item
                continue

            # If line starts with !!!
            elif i[1].startswith("!!!"):

                # Replace first 3 "!"s with """
                i[1] = i[1].replace("!", '"', 3)

                # Append the changed string
                compiledlist.append(i[1])

            # If line doesn't contain ":"
            elif ":" not in i[1]:

                # Strip all spaces
                i[1] = i[1].strip(" ")

                # Add "()" to the end
                i[1] = i[1] + "()"

                # Append the changed string
                compiledlist.append(i[1])

            # If line contains ":"
            elif ":" in i[1]:

                # Replace the ":"" with "()"
                i[1] = i[1].replace(":", "(", 1)

                # Append ")" at the end
                i[1] += ")"

                # Append the changed string
                compiledlist.append(i[1])

            return compiledlist

        except Exception as _:

            # Raise error for compilation
            raise CompilationError(
                "An error has occurred while compiling. Line {1} is \
                causing this issue.".format(i[0]))

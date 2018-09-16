# Import module to get execution arguments
from sys import argv as args

# Import module to check if file exists
import os

# Import module to exit execution
from sys import exit as exitexc

# Import module to generate SHA256 hash
from services.hashing import gethash

# Import module to exexute external commands


def executepyfile(filename):

    # Execute each line of a file
    for i in enumerate(open(str(filename)).read().splitlines()):

        # Try to execute the command
        try:

            # Catch any execution exception
            exec(i[1])

        except Exception as exc:

            # Print the exception text
            print(
                "ERROR: An error of type {0} occured while running line {1} because {2}"
                .format(type(exc).__name__, str(i[0] + 1), str(exc.args[0])))

            # Exit the execution with a value of 1
            exitexc(1)


# Check if file provided in execution arguments
try:

    # Try to evalute the second execution argument (file name)
    args[1]

# Check for a evaluation error (file name not specified)
except IndexError:

    # Throw an error
    print("ERROR: No ROS Code file provided in execution arguments")

    # Stop execution
    exitexc(1)

# Check if file exists
if not os.path.isfile(args[1]):

    # Throw an error
    print("ERROR: " + args[1] + " is not found.")

    # Stop execution
    exitexc(1)

# Check if cached file exists
if os.path.isfile("__roscache__/cache-" +
                  gethash(args[1].split("\\")[-1].split("/")[-1])):

    execlist = [
        "python", "./__roscache__/cache-" + gethash(
            args[1].split("\\")[-1].split("/")[-1])
    ]

    for i in range(2, len(args)):
        execlist.append(args[i])

if os.path.isdir("/home/el"):
    pass

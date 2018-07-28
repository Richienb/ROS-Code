"""
Encodes and runs a ROS Code file
"""
# Main Modules
from sys import argv as args
from sys import exit as exitexc
from ros import main
import importlib
import os.path

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

# Open the file as read only mode
f = open(args[1], "r")

# Set the ignoreline variable for ignoring whole lines
IGNORELINE = False

# Read all the lines in the file to a variable
CONTENT = f.readlines()

# Remove all the blank strings from the variable
CONTENT = [x.strip() for x in CONTENT if x.strip()]

# For every line in the text file
for value in enumerate(CONTENT):

    # Check if the line doesn't start with "!" and if ignoreline is false
    if not (value[1].startswith('!')) and IGNORELINE is False:

        # Check if value starts with "mod" for custom ROS module
        if value[1].startswith('mod'):

            # Try to import the module
            try:

                # Import the module
                importlib.import_module("ros." + value[1].split(" ")[1])

                # Catch a module not found
            except ModuleNotFoundError:

                # Raise a runtime error
                raise ImportError("Error: Unable to import")

                # Exit the execution
                exitexc(1)

                # Check if the value starts with "ext" for custom user module
        elif value[1].startswith('ext'):

            # Check if the file exists
            if os.path.isfile(value[1].split(" ")[1] + ".ros"):
                pass  # TODO: Allow importing of external packages

        # Check if the value starts with "imp" for custom python file
        elif value[1].startswith('imp'):

            # Check if the file exists
            if os.path.isfile(value[1].split(" ")[1] + ".py"):

                # Import the module
                importlib.import_module(value[1].split(" ")[1])

        # Render the command

        # Get the first part of the command - the module used
        part_mod = value[1].split(".")[0]

        # Get the second part of the command - the command used
        part_cmd = value[1].split(".")[1]

        # Get all the content past the mod and cmd
        part_args1 = value[1][(len(part_mod) + 1) + (len(part_cmd) + 1):]

        # Add quotes around each item to a list
        part_args2 = []
        for part in enumerate(part_args1.split(".")):
            part_args2.append('"' + str(part[1]) + '"')

        # Convert the list to a string and remove the box brackets
        part_args = str(part_args2).strip("[").strip("]")

        # Generate the final code to execute
        final = part_mod + "." + part_cmd + "(" + part_args + ")"

        # Try to execute the command
        try:

            # Execute the command
            exec(str(final))

        # Catch any execution exception
        except Exception as exc:

            # Set the template for the exception
            template = "ERROR: An error of type {0} occured while running line {1} because {2}"

            # Format the template
            message = template.format(
                type(exc).__name__, str(value[0] + 1), str(exc.args[0]))

            # Print the exception text
            print(message)

            # Exit the execution with a value of 1
            exitexc(1)

    # Check if the value starts with a grouped comment
    elif value[1].startswith('!!!'):

        # Set the ignoreline variable
        IGNORELINE = not IGNORELINE

# Close the file reader
f.close()

# Exit the execution with 0
exitexc(0)

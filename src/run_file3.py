import os
from sys import argv as args
from sys import exit
from importlib import import_module
import re


def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda: f.read(128 * 1024), b''):
            h.update(b)
    return h.hexdigest()


# __roscache__ folder exists?
if not os.path.exists("__roscache__"):
    # Create __roscache__ folder
    os.makedirs("__roscache__")

# Get hash of file
file_hash = sha256sum(args[1])

# __roscache__/FILE_HASH.py exists?
if os.path.exists("__roscache__/" + file_hash + ".py"):
    # Runtime error (catch)?
    try:
        # Execute file
        import_module("__roscache__." + file_hash)

    except ex as Exception():
        # Print problem in readable format
        print(template="ERROR: An error of type {0} occured because {2}".format(
            type(exc).__name__, str(value[0] + 1), str(exc.args[0])))

        # Exit the execution with a value of 1
        exit(1)

    else:
        # Exit the execution with a value of 0
        exit(0)

# Convert input file to a list
with open(args[1]) as f:
    file_contents = f.read().splitlines()

# Create a blank list
new_file_contents = []

# Set ignoreline variable to False
ignoreline = False

# For loop
for i in enumerate(file_contents):
    # Blank line?
    if i[1] == "" or ignoreline == True:
        # Append to list
        new_file_contents.append("")

    # Starts with "!!!"?
    elif i[1].startswith("!!!"):
        # Set ignoreline variable to True
        ignoreline = not ignoreline

        # Replace with """ and append
        new_file_contents.append(i[1].replace("!!!", "\"\"\"", 1))

    # First character "!"?
    elif i[1].startswith("!"):
        # Replace with "#" and append
        new_file_contents.append(i[1].replace("!", "#", 1))

    # Doesn't contain : (or escaped)
    elif not re.compile(r"(?<!\\):").search(i[1]):
        # Add () to the end and append
        new_file_contents.append(i[1] + "()")

    # Contains ":" (not escaped)
    elif re.compile(r"(?<!\\):").search(i[1]):
        # Replace ":" with "("
        i[1].replace(":", "(", 1)

        # Add ")" at the end of the arguments
        i[1] += ")"

    else:
        # Throw compilation error
        print("An error occurred while parsing line {0}.".format(i[0]))

        # Exit the execution with a value of 1
        exit(1)

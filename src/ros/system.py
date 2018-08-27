# System modules
import subprocess
import os
import sys
import logging
import pkg_resources
import clipboard
from roserrors import *

# Get The Current Platform


def getplatform():
    return sys.platform


def shellcommand(command):
    """

    Execute a command in the host's terminal/shell/bash

    command:
    Specify the command to be executed

    """

    subprocess.call(str(command))


def pipupdate():
    """

    Update all currently installed pip packages

    """

    packages = [d for d in pkg_resources.working_set]
    subprocess.call('pip install --upgrade ' + ' '.join(packages))


# Tools For Directories (If Exists, Make And Delete)


def dirtool(operation, directory):
    operation = operation.lower()
    if operation == 'exists':
        return bool(os.path.exists(directory))
    if operation == 'create':
        if os.path.exists(directory):
            raise RuntimeError(
                'An Error Has Occured: Directory Already Exists (0007)')
        else:
            os.makedirs(directory)
    elif operation == 'delete':
        if os.path.exists(directory):
            os.rmdir(directory)
        else:
            raise RuntimeError(
                'An Error Has Occured: Directory Doesn\'t Exist (0009)')
    else:
        raise RuntimeError(
            'An Error Has Occured: Invalid Operation Entered (0008)')


# Tools For Files (If Exists, Make And Delete)


def file(operation, path):
    operation = operation.lower()
    if operation == 'exists':
        return bool(os.path.isfile(path))
    if operation == 'read':
        if os.path.isfile(path):
            with open(path, 'r') as f:
                return [line.strip() for line in f]
        raise RuntimeError('An Error Has Occured: File Not Found (0012)')
    elif operation == 'delete':
        if os.path.isfile(path):
            os.remove(path)
        else:
            raise RuntimeError('An Error Has Occured: File Not Found (0012)')
    elif operation == 'create':
        if not file('exists', path):
            open(path, 'w').close()
        else:
            raise RuntimeError(
                'An Error Has Occured: File Already Exists (0013)')
    elif operation == 'clear':
        if os.path.isfile(path):
            open(path, 'w').close()
        raise RuntimeError('An Error Has Occured: File Not Found (0012)')
    else:
        raise RuntimeError(
            'An Error Has Occured: Invalid Operation Entered (0008)')


# Exit the current execution


def exitexecution(arguments=0):
    sys.exit(arguments)


# Get The Character Limit


def charlimit():
    return sys.maxsize


# Get The Highest Unicode Value


def unilimit():
    return sys.maxunicode


# Get the version of Python


def pyversion(part=None):
    if part is None:
        return sys.version_info
    return sys.version_info[part]


# Get the executable used by Python


def pyexec():
    return sys.executable


# Print Python copyright information


def pycopyright():
    return sys.copyright


# Set logging status dependant on if debug is enabled


def loglevel(leveltype=None, isequal=False):
    """

    Set the logging level of ROS Code

    without arguments:
    Gives you the logging level

    leveltype:
    Choose the logging level. Possible choices are none (0), debug (10), info (20), warning (30), error (40) and critical (50)

    isequal:
    Instead of setting the level, returns True if the level is equal to leveltype. Otherwise, returns False

    """
    leveltype = leveltype.lower()
    loglevels = {
        "none": 0,
        "debug": 10,
        "info": 20,
        "warning": 30,
        "error": 40,
        "critical": 50
    }
    if leveltype is None and isequal is False:
        return logging.getEffectiveLevel()
    if leveltype is not None and isequal is True:
        if leveltype in loglevels.values():
            return leveltype == logging.getEffectiveLevel()
        elif leveltype in loglevels:
            return loglevels[leveltype] == logging.getEffectiveLevel()
        else:
            raise WrongInput(
                "Incorrect input provided. It should be none, debug, info, warning, error or critical"
            )
    if leveltype in loglevels.values():
        logging.basicConfig(level=leveltype)
    elif leveltype in loglevels:
        logging.basicConfig(level=loglevels[leveltype])
    else:
        raise WrongInput(
            "Incorrect input provided. It should be none, debug, info, warning, error or critical"
        )


def logfile(targetfile="ros.log"):
    """

    Set the file for ROS Code to log to

    targetfile:
    Change the file to log to. By default it is ros.log

    """

    try:
        str(targetfile)
    except BaseException:
        raise ConversionError("Cannot convert type " + str(type(targetfile)) +
                              "to str")
    try:
        logging.basicConfig(filename=str(targetfile))
    except BaseException:
        raise WrongInput("Invalid target file specified")


# Gets, sets, appends or preceeds the clipboard contents


def clipaction(action='get', text=None):
    if action == 'get':
        return clipboard.paste()
    elif action == 'set':
        clipboard.copy(str(text))
    elif action == 'append':
        clipboard.copy(str(clipboard.paste) + str(text))
    elif action == 'preceed':
        clipboard.copy(str(text) + str(clipboard.paste))


# Tools For Text Files


def text(operation, path, argument):
    operation = operation.lower()
    if operation == 'write':
        if os.path.isfile(path):
            fh = open(path, 'w')
            fh.write(argument)
        else:
            raise RuntimeError('An Error Has Occured: File Not Found (0012)')
    elif operation == 'append':
        if os.path.isfile(path):
            fh = open(path, 'a')
            fh.write(argument)
        else:
            raise RuntimeError('An Error Has Occured: File Not Found (0012)')

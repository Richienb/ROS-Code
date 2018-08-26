"""

ROS Code Commands
This file contains all the commands in ROS Code

"""

# Python modules
import warnings
import keyword
import importlib

# String modues
import string
import textwrap
import pprint

# External Modules
import loremipsum
import colour

# Custom modules
from . import roserrors


# Show a shell based input line and return command and parameters


def shellinput(initialtext='>> ', splitpart=' '):
    """

    Give the user a shell like interface to enter commands which are returned as a multi part list containing the command and each of the arguments

    initialtext:
    Set the text to be displayed as the prompt. Default is '>>'.

    splitpart:
    The character to split when generating the list item. Default is ' '. Set to '' or None to skip splitting.

    """

    try:
        str(initialtext)
    except BaseException:
        raise ConversionError("Cannot convert type " + str(type(initialtext)) +
                              "to str")
    shelluserinput = input(str(initialtext))
    if splitpart == '' or splitpart is None:
        return shelluserinput
    commands = []
    for item in enumerate(shelluserinput.split(splitpart)):
        commands.append(item[1])
    return commands


def colourcode(startcolourcode, destinationtype, longhex=False):
    """

    Convert a colour code from one format to another

    startcolourcode:
    Set the colour code to convert from

    destinationtype:
    Set the colour code type to convert to. Possible options are hex, hsl, rgb, red, blue, green, hue, sat and lum

    longhex:
    If converting to hex, provided the long and unsimplified version. Default is False.

    """

    c = colour.Color(str(startcolourcode))
    if destinationtype.lower() == 'hex':
        if longhex is True:
            return c.hex_l
        return c.hex
    elif destinationtype.lower() == 'hsl':
        return c.hsl
    elif destinationtype.lower() == 'rgb':
        return c.rgb
    elif destinationtype.lower() == 'red':
        return c.red
    elif destinationtype.lower() == 'blue':
        return c.blue
    elif destinationtype.lower() == 'green':
        return c.green
    elif destinationtype.lower() == 'hue':
        return c.hue
    elif destinationtype.lower() == 'sat':
        return c.saturation
    elif destinationtype.lower() == 'lum':
        return c.luminance
    raise WrongInput("Destination colour code not specified correctly")


def changecolour(colourcode, action, amount=100):
    """

    Modify a parameter of a colour code

    colourcode:
    The colourcode representing the colour to convert from.

    action:
    The action to perform on the colour. Possible options are red, blue, green, hue, sat, lum

    amount:
    The percentage of the action to perform. For example: 100 means apply 100% of the colour (no change). Default is 100.

    """

    c = colour.Color(colourcode)
    if action == 'red':
        c.red = amount / 100
        return c
    elif action == 'blue':
        c.blue = amount / 100
        return c
    elif action == 'green':
        c.green = amount / 100
        return c
    elif action == 'hue':
        c.hue = amount / 100
        return c
    elif action == 'sat':
        c.saturation = amount / 100
        return c
    elif action == 'lum':
        c.luminance = amount / 100
        return c


def leadingzero(number, minlength):
    """

    Add leading zeros to a number

    number:
    Number to add the leading zeros to

    minlength:
    If the number is shorter than this length than add leading zeros to make the length correct

    """

    return str(number).zfill(int(minlength))


def absolutenum(number):
    """

    Get the absolute value for a number

    number:
    The number to get the absolute value for

    """

    return abs(number)


def splitstring(string, split_character=' ', part=None):
    """

    Split a string based on a character and get the parts as a list

    string:
    The string to split

    split_character:
    The character to split for the string. Default is ' '.

    part:
    Get a specific part of the list. Default is None.

    """

    if part is None:
        return str(string).split(split_character)
    return str(string).split(split_character)[part]


def sort(listtosort, key=None, reversesort=False):
    """

    Sort a list alphabetically

    listtosort:
    The list which will be sorted

    key:
    The key to use when sorting. Default is None.

    reverse:
    If to sort backwards. Default is False.

    """

    return sorted(listtosort, key=key, reverse=reversesort)


def pykeyword(operation='list', keywordtotest=None):
    """

    Check if a keyword exists in the Python keyword dictionary

    operation:
    Whether to list or check the keywords. Possible options are list and check. Default is 'list'.

    keywordtotest:
    The keyword to test for if operation is 'check'. Default is None.

    """

    if operation == 'list':
        return str(keyword.kwlist)
    elif operation == 'check':
        return keyword.iskeyword(str(keywordtotest))

# Pretty print a list


def prettyprinter(listtoprint, stream=None, indent=1, width=80, depth=None):
    pprint.pprint(listtoprint, stream, indent, width, depth)


# Generate a string of Lorem Ipsum


def genipsum():
    # TODO: Make this work.
    # https://loremipsum.readthedocs.io/en/latest/#api
    pass


# Convert 0 or 1 to False or True


def bintobool(integer):
    if isinteger(integer) and integer < 2 and integer > -1:
        if integer == 0:
            return False
        elif integer == 1:
            return True


# Reload a module


def modulereload(modulename):
    importlib.reload(modulename)


# Configure the Python warnings


def warnconfig(action='default'):
    if action == 'default':
        warnings.filterwarnings('default')
    elif action == 'error':
        warnings.filterwarnings('error')
    elif action == 'ignore':
        warnings.filterwarnings('ignore')
    elif action == 'always':
        warnings.filterwarnings('always')
    elif action == 'module':
        warnings.filterwarnings('module')
    elif action == 'once':
        warnings.filterwarnings('once')


# Print a console message


def message_print(text, amount=1):
    for _ in range(amount):
        print(text)





# Get The Sides Of A Shape


def shapesides(inputtocheck, inputtype='shape'):
    inputtocheck = inputtocheck.lower()
    shapestosides = {
        'triangle': 3,
        'square': 4,
        'pentagon': 5,
        'hexagon': 6,
        'heptagon': 7,
        'octagon': 8,
        'nonagon': 9,
        'decagon': 10,
        'hendecagon': 11,
        'dodecagon': 12,
        'triskaidecagon': 13,
        'tetrakaidecagon': 14,
        'pentadecagon': 15,
        'hexakaidecagon': 16,
        'heptadecagon': 17,
        'octakaidecagon': 18,
        'enneadecagon': 19,
        'Icosagon': 20,
        'triacontagon': 30,
        'tetracontagon': 40,
        'pentacontagon': 50,
        'hexacontagon': 60,
        'heptacontagon': 70,
        'octacontagon': 80,
        'enneacontagon': 90,
        'hectagon': 100,
        'chiliagon': 1000,
        'myriagon': 10000,
        'megagon': 1000000,
        'googolgon': pow(10, 100)
    }
    if inputtype == 'shape':
        if inputtocheck in shapestosides:
            return shapestosides[inputtocheck]
        return "ngon"

# Check If A Value Is Able To Be Converted To A Number (Decimal And Integer)


def _isnum(value):
    try:
        return bool(isinstance(value, int) or isinstance(value, float))
    except BaseException:
        return False_


# Compare 2 Numbers


def comparenum(value1, value2, comparison):
    if _isnum(value1) and _isnum(value2):
        comparison = comparison.lower()
        if comparison == 'equals':
            return value1 == value2
        elif comparison == 'not equal':
            return value1 != value2
        elif comparison == 'less than':
            return value1 < value2
        elif comparison == 'greater than':
            return value1 > value2
        elif comparison == 'more than':
            return value1 > value2
        elif comparison == 'less than or equal to':
            return value1 <= value2
        elif comparison == 'greater than or equal to':
            return value1 >= value2
        elif comparison == 'more than or equal to':
            return value1 >= value2














# Throw A Runtime Error


def throwerror(errortext):
    raise RuntimeError("Forced Error: " + str(errortext))


# Store A Value In The __ros_stored__ Variable


def store(value):
    global __ros_stored__
    __ros_stored__ = value


# Get The Stored Variable


def getstored():
    return __ros_stored__


# Delay For A Specific Amount Of Seconds


def delay(seconds):
    time.sleep(seconds)


# Waits For The User To Press Enter


def wait_enter(times=1):
    for _ in range(times):
        input('')


# Convert A Variable To A String


def convertstring(value):
    return str(value)


# Return The Opposite Of A Boolean


def opposite(boolean):
    try:
        return not boolean
    except BaseException:
        raise RuntimeError(
            'An Error Has Occured: Nor A Bool Or Len Was Provided (0014)')


# Check If A Number Is A Decimal


def isdecimal(value):
    return bool(isinstance(value, float))


# Check If A Variable Is A String


def isstring(variable):
    return bool(isinstance(variable, str))


# Check If A Variable Is A Specific Type


def istype(variable, typeexpected):
    return bool(isinstance(variable, typeexpected))


# Check If A Number Is An Integer (Full Number)


def isinteger(value):
    return bool(isinstance(value, int))


# Check For A Boolean


def isboolean(value):
    return isinstance(value, bool)


# Sing Happy Birthday


def happybirthday(person):
    print('Happy Birthday To You')
    time.sleep(2)
    print('Happy Birthday To You')
    time.sleep(2)
    print('Happy Birthday Dear ' + str(case(person, argument='sentence')))
    time.sleep(2)
    print('Happy Birthday To You')


# Change The Casing Of Text


def case(variable, argument='uppercase'):
    if argument == 'uppercase':
        return variable.upper()
    elif argument == 'lowercase':
        return variable.lower()
    elif argument == 'sentence':
        return str(variable[0].upper()) + str(variable[1:])


# Find The Difference Between 2 Numbers


def difference(num1, num2):
    return abs(num1 - num2)


# Check If A Number Is Divisible By Another Number


def divisable(num1, num2):
    return bool(num1 % num2 == 0)


# Check If A Variable Is Empty


def isempty(variable):
    return bool(variable == '')


# Find The Length Of A Value


def length(value):
    try:
        return len(convertstring(value))
    except OverflowError:
        raise RuntimeError(
            'An Error Has Occured: The length of the object exceeds \
        the limit of {0}'.format(str((charlimit()))))


# Simulate A Cow Saying Text


def cowsay(text='', align='centre'):
    align = align.lower()
    cowtext = str(text)
    topbar = ' '
    bottombar = ' '
    spacing = ''
    for _ in range(len(text) + 2):
        topbar = topbar + '_'
        bottombar = bottombar + '-'
    if align in ["center", "centre"]:
        for _ in range((int(len(topbar) / 2)) + 1):
            spacing = spacing + ' '
    elif align == 'left':
        spacing = ' '
    elif align == 'right':
        for _ in range(len(text) + 2):
            spacing = spacing + ' '
    print(topbar)
    print('( ' + cowtext + ' )')
    print(bottombar)
    print(spacing + r'o   ^__^ ')
    print(spacing + r' o  (oO)\_______')
    print(spacing + r'    (__)\       )\/\ ')
    print(spacing + r'     U  ||----w | ')
    print(spacing + r'        ||     || ')


# Get The Corresponding Letter In A String


def getletter(variable, letternumber):
    return str(variable)[letternumber - 1]


# Check If Something Is On The List


def onlist(listtocheck, item):
    return item in listtocheck


# Join Two Strings


def jointext(firststring, secondstring):
    return str(firststring) + str(secondstring)


# About Information


def about():
    print('You Are Using ROS Code')
    print('ROS Code Is licensed Under The Apache License 2.0')
    print('Type "ros.license()" To Read The license')


# Get the value of __name__


def pyname(ifmain=False):
    if ifmain is True:
        return __name__ == "__main__"
    return __name__


# Convert Text To Binary Form


def convertbinary(value, argument):
    if argument == 'to':
        try:
            return bin(value)
        except BaseException:
            raise RuntimeError('Invalid Value (0016)')
    elif argument == 'from':
        try:
            return format(value)
        except BaseException:
            raise RuntimeError('Invalid Value (0016)')


# Make The Text Forwards Or Backwards


def reversetext(texttoreverse, ignoretype=False):
    if ignoretype is False:
        if isinteger(texttoreverse):
            return int(str(texttoreverse)[::-1])
        elif isdecimal(texttoreverse):
            return float(str(texttoreverse)[::-1])
        return str(texttoreverse)[::-1]
    return str(texttoreverse)[::-1]


# Reverse A List


def reverselist(listtoreverse):
    return listtoreverse.reverse()


# Replace Text In A Variable


def replacetext(string, texttofind, texttoreplace):
    return string.replace(texttofind, texttoreplace)





# Get User input


def userinput(prompttext):
    try:
        return input(prompttext)
    except BaseException:
        return input(str(prompttext))

# Evaluate A Expression Or Operation


def evaluate(evaluation):
    return eval(str(evaluation))


# Execute A Line Of Python Code


def execute(execution):
    exec(str(execution))


# Get The Type Of A Value


def gettype(value):
    return type(value)

# Do a quick module test


def pingtest(returntrue=False):
    if returntrue:
        return True
    print("Pong!")


# Convert A ASCII Value To A Symbol


def convertascii(value, command='to'):
    command = command.lower()
    if command == 'to':
        try:
            return chr(value)
        except ValueError:
            raise RuntimeError('Invalid Symbol Value (0014)')
    elif command == 'from':
        try:
            return ord(value)
        except ValueError:
            raise RuntimeError('Invalid Symbol (0015)')
    else:
        raise RuntimeError(
            'An Error Has Occured: Invalid Operation Entered (0008)')


# Get All Available Characters For A Type


def availchar(charactertype):
    if charactertype == 'letters':
        return string.ascii_letters
    elif charactertype == 'lowercase':
        return string.ascii_lowercase
    elif charactertype == 'uppercase':
        return string.ascii_uppercase
    elif charactertype == 'digits':
        return string.digits
    elif charactertype == 'hexdigits':
        return string.hexdigits
    elif charactertype == 'punctuation':
        return string.punctuation
    elif charactertype == 'printable':
        return string.printable
    elif charactertype == 'whitespace':
        return string.whitespace
    else:
        raise RuntimeError(
            'An Error Has Occured: Invalid Operation Entered (0008)')


# Get The Value Of A Word


def wordvalue(word):
    total = 0
    for i in enumerate(word):
        total += letternum(word[i])
    return total


# Get the Range Of The Length


def enum(arguments):
    return enumerate(arguments)


# Get The Text Between Two Parts


def textbetween(variable,
                firstnum=None,
                secondnum=None,
                locationoftext='regular'):
    if locationoftext == 'regular':
        return variable[firstnum:secondnum]
    elif locationoftext == 'toend':
        return variable[firstnum:]
    elif locationoftext == 'tostart':
        return variable[:secondnum]


# Get The Number Corresponding To A Letter


def letternum(letter):
    if len(letter) == 1 and isstring(letter):
        letter = letter.lower
        alphaletters = availchar('lowercase')
        for i in range(len(alphaletters)):
            if getletter(letter, 1) == getletter(alphaletters, i + 1):
                return i + 1








# Return The List Equally Spaced


def spacelist(listtospace):
    output = ''
    space = ''
    output += str(listtospace[0])
    space += ' '
    for listnum in range(1, len(listtospace)):
        output += space
        output += str(listtospace[listnum])
    return output


# List Or Count The Numbers Between Two Numbers


def numlistbetween(num1, num2, option='list', listoption='string'):
    if option == 'list':
        if listoption == 'string':
            output = ''
            output += str(num1)
            for currentnum in range(num1 + 1, num2 + 1):
                output += ','
                output += str(currentnum)
        elif listoption == 'list':
            output = []
            for currentnum in range(num1, num2 + 1):
                output.append(str(currentnum))
            return output
    elif option == 'count':
        return num2 - num1


# Align Text When Given Full Length


def textalign(text, maxlength, align='left'):
    spaces = ''
    if align == 'left':
        return text
    elif align == 'centre' or align == 'center':
        for _ in range(int((maxlength - len(text)) / 2)):
            spaces += ' '
    elif align == 'right':
        for _ in range(maxlength - len(text)):
            spaces += ' '
    return spaces + text





# Fix The Formatting Of Decimals And Integers


def decintfix(decorint=0):
    if str(decorint)[-2:] == '.0':
        return int(decorint)
    return float(decorint)





# License Information


def roslicense(raw=False):
    if raw is False:
        print('ROS Code is licensed under the Apache License 2.0')
        print(
            u'\u2714' +
            ' Permissions: Commercial use, Modification, Distribution, Patent use And Private use'
        )
        print(u'\u274c' + ' Limitations: Trademark use, Liability And Warranty')
        print(u'\u2139' +
              ' Conditions: License and copyright notice And State changes')
        print(
            'To View The Full license, Go To: https://rosurl.ga/ROS-Code-license'
        )
    else:
        print('ROS Code Is licensed Under The Apache License 2.0')
        print(
            'Permissions: Commercial use, Modification, Distribution, Patent use And Private use'
        )
        print('Limitations: Trademark use, Liability And Warranty')
        print('Conditions: License and copyright notice And State changes')
        print(
            'To View The Full license, Go To: https://rosurl.ga/ROS-Code-license'
        )

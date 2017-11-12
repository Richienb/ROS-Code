# Start ROS Code

print('Loading ROS Code')

# Prepare Debug Enabled Variable For Toggling Debug Mode
def debug_debugstatesetup():
	global debugenabled
	debugenabled = False

debug_debugstatesetup()

# DEBUG: Enable Or Disable Debug Mode
def debugstate(state):
    if state == 'Enable':
        debugenabled = True
        print('Debug Mode Has Been Enabled')
    elif state == 'Disable':
        debugenabled = False
        print('Debug Mode Has Been Disabled')
    else:
        raise RuntimeError('An Error Has Occured: Invalid Debug State Entered (0005)')
		
# DEBUG: Make ROS Code Variables Global
def debug_varglobal():
	if debugenabled == True:
		global ros_output
		global ros_stored
	else:
		raise RuntimeError('An Error Has Occured: Debug Mode Not Enabled (0006)')
		
# DEBUG: Supress All Warnings
def debug_supresswarnings():
	if debugenabled == True:
		import warnings
		warnings.filterwarnings("ignore")
	else:
		raise RuntimeError('An Error Has Occured: Debug Mode Not Enabled (0006)')

# Check If A Number Is A Prime Number
def isprime(number):
	if number == 1:
		return False
	for i in range(2,int(number**0.5)+1):
		if number%i==0:
			return False
	return True
	
# Make A Paragraph Space
def paraspace(paragraphspaces=1):
	for i in range(paragraphspaces):
			print('', end='\n')
			
# Split A String
def splitstring(string, split_character=' '):
	return string.split(split_character)
	
# Sort A List
def sort(list, key=None):
	if key == None:
		return sorted(list)
	return sorted(list, key)

# Check If A Keyword Relates To Python
def pykeyword(operation='list', keywordtotest=None):
	import keyword
	if operation == 'list':
		return str(keyword.kwlist)
	elif operation == 'check':
		return keyword.iskeyword(str(keywordtotest))
		
# Convert 0 Or 1 To False Or True
def bintobool(integer):
	if isinteger(integer) and integer < 2 and integer > -1:
		if integer == 0:
			return False
		elif integer == 1:
			return True

# Reload A Module
def modulereload(modulename):
	import importlib
	importlib.reload(modulename)

# Exit The Execution
def exitexecution(arguments=None):
	import sys
	sys.exit(arguments)

# Configure Warnings
def warnconfig(action='default'):
	import warnings
	if action == 'default':
		warnings.filterwarnings("default")
	elif action == 'error':
		warnings.filterwarnings("error")
	elif action == 'ignore':
		warnings.filterwarnings("ignore")
	elif action == 'always':
		warnings.filterwarnings("always")
	elif action == 'module':
		warnings.filterwarnings("module")
	elif action == 'once':
		warnings.filterwarnings("once")
		
# Print Python Copyright Information
def pycopyright():
	import sys
	return sys.copyright

# Print A Message
def message_print(text):
	print(text)
	
# Solve A Maths Equation
def equation(operation, firstnum, secondnum):
	if not isnumber(firstnum) and isnumber(secondnum):
		raise RuntimeError('An Error Has Occured: One Of The Values Specified Is Not A Number (0002)')
	if operation == 'plus':
		return (firstnum + secondnum)
	elif operation == 'minus':
		return (firstnum - secondnum)
	elif operation == 'multiply':
		return (firstnum * secondnum)
	elif operation == 'divide':
		return (firstnum / secondnum)
	else:
		raise RuntimeError('An Error Has Occured: You Entered An Invalid Operation (0003)')

# Preform Scientific Operations
def scientific(number, operation, logbase=10):
	import math
	if operation == 'log':
		return math.log(number, logbase)
	elif operation == 'acos':
		return math.acos(number)
	elif operation == 'asin':
		return math.asin(number)
	elif operation == 'atan':
		return math.atan(number)
	elif operation == 'cos':
		return math.cos(number)
	elif operation == 'hypot':
		return math.hypot(number)
	elif operation == 'sin':
		return math.sin(number)
	elif operation == 'tan':
		return math.tan(number)

# Compare 2 Values
def compare(value1, value2, comparision):
	import operator
	if comparision == 'is':
		return operator.is_(value1, value2)
	elif comparision == 'or':
		return operator.or_(value1, value2)
	elif comparision == 'and':
		return operator.and_(value1, value2)
		
# Compare 2 Numbers
def comparenum(value1, value2, comparison):
	if isnumber(value1) and isnumber(value2):
		comparison = case(comparison, 'lowercase')
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
			
# Get The Day Of The Week For A Specific Day
def dayofweek(day, month, year, format=True):
	import calendar
	if format == False:
		return calendar.weekday(year, month, day) + 1
	else:
		if calendar.weekday(year, month, day) == 0:
			return 'Monday'
		elif calendar.weekday(year, month, day) == 1:
			return 'Tuesday'
		elif calendar.weekday(year, month, day) == 2:
			return 'Wednesday'
		elif calendar.weekday(year, month, day) == 3:
			return 'Thursday'
		elif calendar.weekday(year, month, day) == 4:
			return 'Friday'
		elif calendar.weekday(year, month, day) == 5:
			return 'Saturday'
		elif calendar.weekday(year, month, day) == 6:
			return 'Sunday'
			
# Check If A Year Is A Leap Year
def leapyear(year, querytype='is'):
	import calendar
	querytype == case(querytype, 'lowercase')
	if querytype == 'is':
		return calendar.isleap(year)
	elif querytype == 'closest':
		return year % 4

# Return A Random String In Hexadecimal
def tokhex(length=10, urlsafe=False):
	import secrets
	if urlsafe == True:
		return secrets.token_urlsafe(length)
	else:
		return secrets.token_hex(length)
	

# Get A Constant
def constant(constanttype):
	import math
	if constanttype == 'pi':
		return math.pi
	elif constanttype == 'e':
		return math.e
	elif constanttype == 'tau':
		return math.tau
	elif constanttype == 'inf':
		return math.inf
	elif constanttype == 'nan':
		return math.nan
	
# Find The Power Of A Number
def power(number, power):
	import math
	return math.pow(number, power)

# Find The Squareroot Of A Number
def squareroot(number):
	import math
	return math.sqrt(number)

# Do An Average Command
def average(numbers, type='mean'):
	import statistics
	try:
		statistics.mean(numbers)
	except:
		raise RuntimeError('An Error Has Occured: List Not Specified (0018)')
	if type == 'mean':
		return statistics.mean(numbers)
	elif type == 'mode':
		return statistics.mode(numbers)
	elif type == 'median':
		return statistics.median(numbers)
	elif type == 'min':
		return min(numbers)
	elif type == 'max':
		return max(numbers)
	elif type == 'range':
		return max(numbers) - min(numbers)
	else:
		raise RuntimeError('An Error Has Occured: You Entered An Invalid Operation (0003)')

# Throw A Runtime Error
def throwerror(errortext):
	raise RuntimeError(errortext, ' (0001)')
	
# Store A Value In The ros_stored Variable
def store(value):
	global ros_stored
	ros_stored = value
	
# Delay For A Specific Amount Of Seconds
def delay(seconds):
    from time import sleep as rosfunc_sleep
    rosfunc_sleep(seconds)
	
# Waits For The User To Press Enter
def wait_enter():
    input('')
	
# Convert A Variable To A String
def convertstring(value):
	return str(value)

# Return The Opposite Of A Boolean
def opposite(boolean):
	try:
		return not boolean
	except:
		raise RuntimeError('An Error Has Occured: Nor A Bool Or Len Was Provided (0014)')
	
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
	
# Check If A Value Is Convertable To A Number (Decimal And Integer)
def isnumber(value):
	try:
		return bool(isinteger(value) or isnumber(value))
	except:
		return False
		
# Change The Casing Of Text
def case(variable, argument='uppercase'):
	if argument == 'uppercase':
		return variable.upper()
	elif argument == 'lowercase':
		return variable.lower()

# Check If A Number Is Even
def iseven(number):
	return number % 2 == 0
	
# Check If A Number Is Odd
def isodd(number):
	return opposite(iseven(number))

# Check If A Variable Is Empty
def isempty(variable):
	return bool(variable == '')
	
# Check If A Variable Is Infinite
def isinfinite(variable):
	import math
	return bool(math.isfinite(variable))
	
# Find The Length Of A Value
def length(value):
	try:
		return len(convertstring(value))
	except OverflowError:
		raise RuntimeError('An Error Has Occured: The Length Exceeds The Limit (', charlimit(), ') (0015)')

# Simulate A Cow Saying Text
def cowsay(text='', align='centre'):
	cowtext = str(text)
	topbar = ' '
	bottombar = ' '
	spacing = ''
	for i in range (len(text) + 2):
		topbar = topbar + '_'
		bottombar = bottombar + '-'
	if align == 'centre' or align == 'center':
		for ii in range ((int(len(topbar) / 2)) + 1):
			spacing = spacing + ' '
	elif align == 'left':
		spacing = ' '
	elif align == 'right':
		for iii in range (len(text) + 2):
			spacing = spacing + ' '
	print(topbar)
	print("( " + cowtext + " )")
	print(bottombar)
	print(spacing + 'o   ^__^ ')
	print(spacing + ' o  (oO)\_______' )
	print(spacing + '    (__)\       )\/\ ')
	print(spacing + '     U  ||----w | ')
	print(spacing + '        ||     || ')
	
# Get The Corresponding Letter In A String
def getletter(variable, letternumber):
	return str(variable)[letternumber - 1]

# Play A Chance Game
def chancegame(gamename='dice'):
	if gamename == 'dice':
		return randomnum(1, 6)
	elif gamename == 'die':
		return randomnum(1, 6)
	elif gamename == 'coin':
		if randomnum(1, 2) == 1:
			return 'Heads'
		else:
			return 'Tails'
	elif gamename == 'truth':
		truthnum = randomnum(1, 4)
		if truthnum == 1:
			return 'Truth'
		elif truthnum == 2:
			return 'Maybe'
		elif truthnum == 3:
			return 'Maybe'
		else:
			return 'Lie'

# Check If Something Is On The List
def onlist(list, item):
	return item in list

# Get The Character Limit
def charlimit():
	import sys
	return sys.maxsize

# Get The Highest Unicode Value
def unilimit():
	import sys
	return sys.maxunicode

# Get The Current Platform
def platform():
	import sys
	return sys.platform

# Get The Largest Integer Less Than Or Equal To
def less_or_equal(number):
	import math
	try:
		return math.floor(number)
	except:
		raise RuntimeError('An Error Has Occured: Number Not Provided (0016)')
		
# Join Two Strings
def jointext(firststring, secondstring):
	return str(firststring) + str(secondstring)

# Tools For Directories (If Exists, Make And Delete)
def dirtool(operation, directory):
	import os
	if operation == 'exists':
		return bool(os.path.exists(directory))
	elif operation == 'create':
		if os.path.exists(directory):
			raise RuntimeError('An Error Has Occured: Directory Already Exists (0007)')
		else:
			os.makedirs(directory)
	elif operation == 'delete':
		if os.path.exists(directory):
			os.rmdir(directory)
		else:
			raise RuntimeError('An Error Has Occured: Directory Doesn\'t Exist (0009)')
	else:
		raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')

# Download A File
def filedownload(source, destination):
	import urllib
	if not isempty(source):
		if not isempty(destination):
			try:
				urllib.request.urlretrieve(source, destination)
			except:
				raise RuntimeError('An Error Has Occured: File Download Error (0010)')
		else:
			raise RuntimeError('An Error Has Occured: Source Or Destination Invalid (0011)')
	else:
		raise RuntimeError('An Error Has Occured: Source Or Destination Invalid (0011)')
	
# Tools For Files (If Exists, Make And Delete)
def file(operation, path):
	if operation == 'exists':
		import os.path
		return bool(os.path.isfile(path))
	elif operation == 'read':
		if file('exists', path):
			F = open(path, "w") 
			return F
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
	elif operation == 'delete':
		import os
		if file('exists', path):
			os.remove(path)
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
	elif operation == 'create':
		if not file('exists', path):
			f = open(path, "w+")
			f.close()
		else:
			raise RuntimeError('An Error Has Occured: File Already Exists (0013)')
	else:
		raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')
	
# Tools For Text Files
def text(operation, path, argument):
	if operation == 'write':
		if file('exists', path):
			fh = open(path, "w")
			fh.write(argument)
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
	elif operation == 'append':
		if file('exists', path):
			fh = open(path, "a") 
			fh.write(argument) 
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
			
# About Information
def about():
	print('You Are Using ROS Code')
	print('ROS Code Is Licenced Under The Apache License 2.0')
	print('Type "ros.licence()" To Read The Licence')
	
# Convert Text To Binary Form
def convertbinary(value, argument):
	if argument == 'to':
		try:
			return bin(value)
		except:
			raise RuntimeError('Invalid Value (0016)')
	elif argument == 'from':
		try:
			return format(value)
		except:
			raise RuntimeError('Invalid Value (0016)')
			
# Make The Text Forwards Or Backwards
def reversetext(text, ignoretype=False):
	if ignoretype == False:
		if isinteger(text):
			start = str(text)
			end = start[::-1]
			return int(end)
		elif isdecimal(text):
			start = str(text)
			end = text[::-1]
			return float(end)
		else:
			return str(text)[::-1]
	else:
		return str(text)[::-1]
		
# Convert A Base 10 Number To A Custom Base
def convertbase(number, base=10):
	import string
	integer = number
	if not integer: return '0'
	sign = 1 if integer > 0 else -1
	alphanum = string.digits + string.ascii_lowercase
	nums = alphanum[:base]
	res = ''
	integer *= sign
	while integer:
                integer, mod = divmod(integer, base)
                res += nums[mod]
	return ('' if sign == 1 else '-') + res[::-1]

# Convert A ASCII Value To A Symbol
def convertsymbol(value, command):
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
		raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')
			
# Get The Type Of A Value
def gettype(value):
	return type(value)
			
# Get All Available Charaters For A Type
def availchar(charactertype):
	import string
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
			raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')

# Get Maximum And Minimum Years
def yearlimit(limittype):
	import datetime
	if limittype == 'min':
			return datetime.MINYEAR
	elif limittype == 'max':
			return datetime.MAXYEAR
	else:
			raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')
			
# Get The Timezone Code
def timezone():
	import time
	return time.timezone
		
# Get A Random Number
def randomnum(minimum, maximum):
	if isnumber(minimum):
		if isnumber(maximum):
			from random import randint as randomnumber
			return randomnumber(minimum, maximum)
		else:
			raise RuntimeError('Invalid Value (0016)')
	else:
		raise RuntimeError('Invalid Value (0016)')
		
# Open A Link In A Webbrowser
def openurl(url):
	import webbrowser
	try:
		webbrowser.open(url)
	except webbrowser.Error:
		raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
		
# Open A Link In A New Window Of A Webbrowser
def newwindow(url):
	import webbrowser
	try:
		webbrowser.open_new(url)
	except webbrowser.Error:
		raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
		
# Open A Link In A New Tab Of A Webbrowser
def newtab(url):
	import webbrowser
	try:
		webbrowser.open_new_tab(url)
	except webbrowser.Error:
		raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
		
# Get The Name Of The Browser Currently Being Used
def getbrowser():
	import webbrowser
	webbrowser.get(using=None)
	
# Choose A Random Item From A List
def randomstr(valuelist):
	from random import choice
	try:
		return choice(valuelist)
	except IndexError:
		raise RuntimeError('An Error Has Occured: List Not Specified (0004)')
		
# Get The Time Since 00:00 On 1 January 1970
def timesince():
	from time import time as time_now
	return time_now()
	
# Get User input
def userinput(prompttext):
	try:
		return input(prompttext)
	except:
		return input(str(prompttext))

# Licence Information
def licence(raw=False):
	if raw == False:
		print('ROS Code Is Licenced Under The Apache License 2.0')
		print(u'\u2714' + ' Permissions: Commercial use, Modification, Distribution, Patent use And Private use')
		print(u'\u274c' + ' Limitations: Trademark use, Liability And Warranty')
		print(u'\u2139' + ' Conditions: License and copyright notice And State changes')
		print('To View The Full Licence, Go To: https://rosurl.ga/ROS-Code-Licence')
	else:
		print('ROS Code Is Licenced Under The Apache License 2.0')
		print('Permissions: Commercial use, Modification, Distribution, Patent use And Private use')
		print('Limitations: Trademark use, Liability And Warranty')
		print('Conditions: License and copyright notice And State changes')
		print('To View The Full Licence, Go To: https://rosurl.ga/ROS-Code-Licence')
	
print('Finished Loading ROS Code')

# End ROS Code

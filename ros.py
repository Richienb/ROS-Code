# Start ROS Code

print('Loading ROS Code')

# Prepare Debug Enabled Variable For Toggling Debug Mode
global debugenabled
debugenabled = False

# DEBUG: Enable Or Disable Debug Mode
def debugstate(state):
	if state == 'Enable':
		debugenabled == True
		print('Debug Mode Has Been Enabled')
	elif state == 'Disable':
		debugenabled == False
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
		
# Print A Message
def message_print(text):
	print(text)
	
# Solve A Maths Equation
def equation(operation, firstnum, secondnum):
	if not isnumber(firstnum) and isnumber(secondnum):
		raise RuntimeError('An Error Has Occured: One Of The Values Specified Is Not A Number (0002)')
		return False
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

# Find The Power Of A Number
def power(number, power):
		return pow(number, power)
	
# Get The Mean Of A List Of Values
def avgmean(values):
	import statistics
	try:
		return statistics.mean(values)
	except StatisticsError:
		raise RuntimeError('An Error Has Occured: List Not Specified (0018)')

# Get The Mode Of A List Of Values
def avgmode(values):
	import statistics
	try:
		return statistics.mode(values)
	except StatisticsError:
		raise RuntimeError('An Error Has Occured: List Not Specified (0018)')

# Get The Median Of A List Of Values
def avgmedian(values):
	import statistics
	try:
		return statistics.median(values)
	except StatisticsError:
		raise RuntimeError('An Error Has Occured: List Not Specified (0018)')

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
    ros_entervar = input('')
	
# Convert A Variable To A String
def convertstring(value):
	return str(value)

# Return The Opposite Of A Boolean
def opposite(boolean):
	try:
		return not boolean
	except:
		raise RuntimeError('An Error Has Occured: Nor A Bool Or Len Was Provided (0014)')
	
# Check If A Number Is A Decimal:
def isdecimal(value):
    try:
        a = float(value)
    except ValueError:
        return False
    else:
        return True
		
# Check If A Number Is An Integer (Full Number):
def isinteger(value):
    try:
        a = float(value)
        b = int(a)
    except ValueError:
        return False
    else:
        return True
		
# Check If A Value Is Convertable To A Number (Decimal And Integer)
def isnumber(value):
	try:
		x = int(value)
	except ValueError:
		return False
	else:
		return True
		
# Check If A Number Is Even
def iseven(number):
	return number % 2 == 0
	
# Check If A Number Is Odd
def isodd(number):
	return opposite(iseven(number))

# Check If A Variable Is Empty
def isempty(variable):
	if variable == '':
		return True
	else:
		return False
	
# Check If A Variable Is Infinite
def isinfinite(variable):
	import math
	if math.isfinite(variable):
		return true
	else:
		return false
	
# Find The Length Of A Value
def length(value):
	try:
		return len(convertstring(value))
	except OverflowError:
		raise RuntimeError('An Error Has Occured: The Length Exceeds The Limit (', charlimit(), ') (0015)')

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
def join(firststring, secondstring):
	return (convertstring(firststring) + convertstring(secondstring)
		
# Tools For Directories (If Exists, Make And Delete)
def directory(operation, directory):
	import os
	if operation == 'exists':
		if os.path.exists(directory):
			return True
		else:
			return False
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
				urllib.urlretrieve(source, destination)
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
		if os.path.isfile(path):
			return True
		else:
			return False
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
			file_object = open(path, "w")
			fh.write(argument)
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
	elif operation == 'append':
		if file('exists', path):
			fh = open(path, "a") 
			fh.write(argument) 
			fh.close 
		else:
			raise RuntimeError('An Error Has Occured: File Not Found (0012)')
			
# About Information
def about():
	print('You Are Using ROS Code')
	print('ROS Code Is Licenced Under The Apache License 2.0')
	print('Type "ros.licence" To Read The Licence')
		
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
			
# Convert Text To Binary Form
def convertbinary(value):
	try:
		return bin(value)
	except ValueError:
		raise RuntimeError('Invalid Value (0016)')
		
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
def randomstr(list):
	from random import choice
	try:
		return choice(list)
	except IndexError:
		raise RuntimeError('An Error Has Occured: List Not Specified (0018)')
		
# Get The Time Since 00:00 On 1 January 1970
def timesince():
	from time import time as time_now
	return time_now()

# Licence Information
def licence():
	print('ROS Code Is Licenced Under The Apache License 2.0')
	print('Permissions: Commercial use, Modification, Distribution, Patent use And Private use')
	print('Limitations: Trademark use, Liability And Warranty')
	print('Conditions: License and copyright notice And State changes')
	print('To View The Full Licence, Go To: https://rosurl.ga/ROS-Code-Licence')
	
print('Finished Loading ROS Code')

# End ROS Code

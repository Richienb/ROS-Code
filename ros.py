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
def equation(operation, firstnum, secondnum, argument):
	if not isnumber(firstnum) and isnumber(secondnum):
		raise RuntimeError('An Error Has Occured: One Of The Values Specified Is Not A Number (0002)')
		return False
	if argument == 'write':
		global ros_output
		if operation == 'plus':
			ros_output = (firstnum + secondnum)
		elif operation == 'minus':
			ros_output = (firstnum - secondnum)
		elif operation == 'multiply':
			ros_output = (firstnum * secondnum)
		elif operation == 'divide':
			ros_output = (firstnum / secondnum)
		else:
			raise RuntimeError('An Error Has Occured: You Entered An Invalid Operation (0003)')
	elif argument == 'print':
		if operation == 'plus':
			print(firstnum + secondnum)
		elif operation == 'minus':
			print(firstnum - secondnum)
		elif operation == 'multiply':
			print(firstnum * secondnum)
		elif operation == 'divide':
			print(firstnum / secondnum)
		else:
			raise RuntimeError('An Error Has Occured: You Entered An Invalid Operation (0003)')
	elif argument == 'return':
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
	else:
		RuntimeError('An Error Has Occured: You Entered An Invalid Output Mehthod (0004)')
		
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
		
# Check If A Value Is Convertable To A Number (Decimal And Integer):
def isnumber(Value):
	valuea = isdecimal(value)
	valueb = isinteger(value)
	if valuea and valueb:
		return True
	else:
		return False
	
# Check If A Variable Is Empty
def isempty(variable):
	if variable == '':
		return true
	else:
		return false

# Tools For Directories (If Exists And Make)
def directory(operation, directory):
	import os
	if operation == 'exists':
		if os.path.exists(directory):
			return true
		else:
			return false
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
	if isempty(source) == False And isempty(destination) == False:
		try:
			urllib.urlretrieve(source, destination)
		except:
			raise RuntimeError('An Error Has Occured: File Download Error (0010)')
	else:
		('An Error Has Occured: Source Or Destination Invalid (0011)')
	
print('Finished Loading ROS Code')

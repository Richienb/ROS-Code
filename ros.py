print('Setting Up And Enabling ROS Code')

def debug_varglobal():
    global ros_output
    global ros_stored
	
def debug_supresswarnings():
    import warnings
    warnings.filterwarnings("ignore")

debug_supresswarnings()
	
def message_print(text):
	print(text)
	
def add_print(firstnum, secondnum):
    print(firstnum + secondnum)

def subtract_print(firstnum, secondnum):
    print(firstnum - secondnum)

def multiply_print(firstnum, secondnum):
    print(firstnum * secondnum)

def divide_print(firstnum, secondnum):
    print(firstnum / secondnum)

def add_write(firstnum, secondnum):
    global ros_output
    ros_output = (firstnum + secondnum)

def subtract_write(firstnum, secondnum):
    global ros_output
    ros_output = (firstnum - secondnum)
	
def multiply_write(firstnum, secondnum):
    global ros_output
    ros_output = (firstnum * secondnum)

def divide_write(firstnum, secondnum):
    global ros_output
    ros_output = (firstnum / secondnum)
	
def equation(operation, firstnum, secondnum, argument):
	if isnumber(firstnum) and isnumber(secondnum):
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
				raise RuntimeError('An Error Has Occured. Error Code: 0003')
		elif argument == 'print':
		
		elif argument == 'return':
			
		else:
			raise RuntimeError('An Error Has Occured. Error Code: 0001')
	else:
		raise RuntimeError('An Error Has Occured. Error Code: 0002')

def error(text):
    raise RuntimeError(text)
	
def errorcode(text, code)
	raise RuntimeError(text, "Error Code: ", code)

def store(value):
    global ros_stored
    ros_stored = value
	
def wait_time(time):
    from time import sleep as rosfunc_sleep
    rosfunc_sleep(time)

def wait_enter():
    ros_entervar = input('')
	
def isdecimal(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True
def isinteger(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b
	
def isnumber(n):
	valuea = isdecimal(n)
	valueb = isinteger(n)
	If valuea() or valueb():
		return True
	Else:
		return False
print('Finished Setting Up ROS Code')

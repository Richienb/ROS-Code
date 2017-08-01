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

def error(text):
    raise RuntimeError(text)

def store(value):
	ros_stored = value
	global ros_stored
	
def wait_time(time):
    from time import sleep
    sleep(time)

def wait_enter():
    ros_entervar = input('')

print('Finished Setting Up ROS Code')

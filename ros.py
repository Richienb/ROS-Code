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
    ros_output = (firstnum + secondnum)
    global ros_output

def subtract_write(firstnum, secondnum):
    ros_output = (firstnum - secondnum)
    global ros_output

def multiply_write(firstnum, secondnum):
    ros_output = (firstnum * secondnum)
    global ros_output

def divide_write(firstnum, secondnum):
    ros_output = (firstnum / secondnum)
    global ros_output

def error(text):
    raise RuntimeError(text)

def store(value):
	ros_stored = value
	global ros_stored

print('Finished Setting Up ROS Code')

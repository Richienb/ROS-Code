print('Setting Up And Enabling ROS Code')

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
  
print('Finished Setting Up ROS Code')

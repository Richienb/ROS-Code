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

def error_print(text):
    raise RuntimeError(text)
  
print('Finished Setting Up ROS Code')

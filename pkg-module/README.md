Thank you for installing the modules of ROS Code.
The installation adds [these](https://github.com/Richienb/ROS-Code/tree/master/min/ros) ([view unminified](https://github.com/Richienb/ROS-Code/tree/master/src/ros)) files in a folder called `ros` in your Python `site-packages` directory.
You can use any commands exposed in that directory

#### Here's an example:

This is how you'd **normally** check if a number is a prime one.
You'd have to create a new function and add a docstring so Python will recognize it when a user executes the `pydoc` command.
Then you'll need to ask for the user's input and execute the command.

```python
def isprime(number):
    """

    Check if a number is a prime number

    number:
    The number to check

    """

    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

if isprime(input("Enter a number to check for prime: ")):
  print("It is prime!")
else:
  print("It isn't prime!")
```

With **ROS Code**, you can simplify this task:

```python
from ros.main import isprime

if isprime(input("Enter a number to check for prime: ")):
  print("It is prime!")
else:
  print("It isn't prime!")
```

You can **find more tasks** which you can simplify related to maths, strings and more [here](https://github.com/Richienb/ROS-Code/tree/master/src/ros).

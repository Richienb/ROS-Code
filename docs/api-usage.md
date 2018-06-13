# Using the ROS Code API

## Usage In The Commandline

```bat
:: This is what you would enter into a batchfile (Windows Terminal - Cmd) to use ROS Code
:: You may need to tinker this to work with your terminal

:: Navigate to the source code directory
cd src

:: Run the compiler with test.ros as input
python run-file.py test.ros
```

___

## Usage In Python

```python
# Ensure you are running this inside the source code directory (src) of the project

# Import the ROS Code python api and rename it to runcode
from rospyapi import compilefile as runcode

# Execute the ROS Code file
runcode("test.ros")
```

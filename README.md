## Welcome To The Official Github Page Of ROS Code
ROS Code is a revolutionary new way to code featuring a fast installation, a simple syntax and is provided as a python library. For more information go to <https://www.ros-code.ga> and to watch the video, go [here](https://www.ros-code.ga/Watch).
___

[![Build Status](https://img.shields.io/travis/Richienb/ROS-Code.svg?style=for-the-badge)](https://travis-ci.org/Richienb/ROS-Code) [![CodeFactor](https://www.codefactor.io/repository/github/richienb/ros-code/badge?style=for-the-badge)](https://www.codefactor.io/repository/github/richienb/ros-code) 

[![GitHub Release](https://img.shields.io/github/release/Richienb/ROS-Code.svg?style=for-the-badge)](https://github.com/Richienb/ROS-Code/releases) [![GitHub Last Commit](https://img.shields.io/github/last-commit/Richienb/ROS-Code.svg?style=for-the-badge)](https://github.com/Richienb/ROS-Code/commits/master)

___

## Installation Instructions
### Refer To [Installation Instructions](https://github.com/Richienb/ROS-Code/wiki/Installation) And [Enabling Guide](https://github.com/Richienb/ROS-Code/wiki/Enable)

___

## Syntax:

Statement separator-terminator: `\n`

Secondary separator: `&`

Line continuation: `-`

Package import: `package module`

Class import: `class module`

Procedure/function import: `function module`

Required to access code: `package module`

Inline comments: `!`

Block comments: `!!!`

___

## Usage In The Commandline:

```batchfile
:: This is what you would enter into a batchfile (Windows Terminal - Cmd) to use ROS Code
:: You may need to tinker this to work with your terminal

:: Clone the repository using git (you could download as zip instead)
git clone https://github.com/Richienb/ROS-Code.git

:: Navigate to the source code directory
cd ROS-Code\src

:: Run the compiler with test.ros as input
python compile.py test.ros
```

___

## Usage In Python:

```python
# Ensure you are running this inside the source code directory (src) of the project

# Import the ROS COde python api and rename it to runcode
from rospyapi import compilefile as runcode

# Execute the ROS Code file
runcode("test.ros")
```

___

> Creator: [Richie Bendall](https://www.richie-bendall.ml)

# Edit the ROS Code source code

### Preparing

- You can find the source code in the `src` directory of the repository.
- The Python 3 runtime for Windows is stored in the `win-runtime` directory.

### How the code works

- The `run-file.py` file is for reading and executing code from a file passed as a runtime variable.

Example:

```bat
python run-file.py test.ros
```

- The `run-line.py` file is for executing a single line of code, passed as a runtime variable.

Example:

```bat
python run-line.py print_message.Hello World
```

- The `syntax.py` file is for storing all the commands.

Example:

```python
def print_message(contents=''):
    print(contents)
```

The code above enables functionality for the `print_message.Hello World` command

- The `run.bat` file is just an easier way to run the following code

```bat
@echo off
python run-file.py test.ros
pause
```

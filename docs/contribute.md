## Edit the documentation

### Preparing

In order to edit the documentation, you will need:

- An installation of Python 3.
- Pip to install `mkdocs` and `mkdocs-material`.

```batchfile
:: Install mkdocs using pip
pip install mkdocs
:: Install mkdocs-material using pip
pip install mkdocs-material
```

After installing mkdocs, start a local server in order to view your changes live.

```batchfile
:: Navigate to the main repository directory
cd C:\ROS-Code
:: Start the mkdocs local server
mkdocs serve
```

Now you can navigate to the URL shown in the terminal (usually [127.0.0.1:8000](http://127.0.0.1:8000)) and you will be able to see the documentation live as you edit it.

### Building

Build the documentation to the `site` folder locally.

```batchfile
:: Build the documentation locally
mkdocs build
```

Deploy the documentation to the `gh-pages` branch in the repository.

```batchfile
:: Deploy the documentation online
mkdocs gh-deploy
```

### Notes

Read the [mkdocs documentation](https://www.mkdocs.org) for more information.

___

## Edit the code

### Preparing

- You can find the source code in the `src` directory of the repository.
- The Python 3 runtime for Windows is stored in the `win-runtime` directory.

### How the code works

- The `run-file.py` file is for reading and executing code from a file passed as a runtime variable.

Example:

```batchfile
python run-file.py test.ros
```

- The `run-line.py` file is for executing a single line of code, passed as a runtime variable.

Example:

```batchfile
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

```batchfile
@echo off
python run-file.py test.ros
pause
```

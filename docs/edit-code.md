# Edit the ROS Code source code

### Preparing

-   You can find the source code in the `src` directory of the repository.
-   The Python 3 runtime for Windows is stored in the `win-runtime` directory.

### How the code works

-   The `run-file.py` file is for reading and executing code from a file passed as a runtime variable.

!!! example "Example"

    ```bat
    python run_file.py test.ros
    ```

-   The files in the `ros` directory are for storing all the commands.

??? example "Example"

    ```python
    def print_message(contents=''):
        print(contents)
    ```

The code above enables functionality for the `print_message: "Hello World"` command

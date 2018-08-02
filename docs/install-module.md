# Install ROS Code as an importable module

!!! warning "Requirement"
    Git must be installed for the steps to work. Travis CI has Git preinstalled.

Use the following code to clone the ROS Code repository and extract the `ros` folder

!!! example "Insert ROS Code as a Python 3.x module in Travis CI"

    ```yml
    install:
      - git clone https://github.com/Richienb/ROS-Code.git
      - mv ./ROS-Code/src/ros .
      - rmdir ./ROS-Code
    ```

!!! example "Insert ROS Code as a Python 3.x module in Terminal"

    ```sh
    $ git clone https://github.com/Richienb/ROS-Code.git
    $ mv ./ROS-Code/src/ros .
    $ rmdir ROS-Code
    ```

!!! example "Insert ROS Code as a Python 3.x module in Windows Cmd"

    ```bat
    git clone https://github.com/Richienb/ROS-Code.git
    move ./ROS-Code/src/ros .
    rmdir ROS-Code
    ```

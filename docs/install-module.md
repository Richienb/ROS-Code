# Install ROS Code as an importable module

Use the following code to clone the ROS Code repository and extract the `
ros.py` file

!!! example "Insert ROS Code as a Python 3.x module in Travis CI"
    ```yml
    install:
      - git clone https://github.com/Richienb/ROS-Code.git
      - mv $PWD/ROS-Code/src/syntax.py $PWD/ROS-Code/src/ros.py
      - cp -r $PWD/ROS-Code/src/ros.py .
      - rmdir $PWD/ROS-Code
    ```

!!! example "Insert ROS Code as a Python 3.x module in Terminal"
    ```sh
    $ git clone https://github.com/Richienb/ROS-Code.git
    $ mv /ROS-Code/src/syntax.py /ROS-Code/src/ros.py
    $ cp -r /ROS-Code/src/ros.py .
    $ rmdir ROS-Code
    ```

!!! example "Insert ROS Code as a Python 3.x module in Windows Cmd"
    ```bat
    git clone https://github.com/Richienb/ROS-Code.git
    rename ROS-Code/src/syntax.py ros.py
    copy ROS-Code/src/ros.py /
    rmdir ROS-Code
    ```

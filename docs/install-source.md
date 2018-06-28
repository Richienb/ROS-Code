# Install ROS Code from source

### Before starting

!!! tip "Prerequisites"
    - [Python 3.x](https://www.python.org/downloads/)
    - [Git](https://git-scm.com/downloads)

!!! tip "Using make?"
    You can simply use a [make](#using-make) command for installing ROS Code

!!! tip "Don't have make?"
    [Skip ahead](#as-a-one-liner) for instructions on running all the commands listed in the installation steps in a single line

### Installation steps

!!! example "Clone the Git repository"
    ```sh
    git clone https://github.com/Richienb/ROS-Code.git
    ```

!!! example "Install the packages required"
    ```sh
    cd ROS-Code
    pip install -r requirements.txt
    cd ..
    ```
!!! example "Rename syntax.py to ros.py"
    Shell/Terminal
    ```sh
    mv $PWD/ROS-Code/src/syntax.py $PWD/ROS-Code/src/ros.py
    ```

    Batch/Cmd/Powershell
    ```bat
    rename /ROS-Code/src/syntax.py ros.py
    ```

!!! example "Fetch the required files"
    Shell/Terminal
    ```sh
    cp ROS-Code/src/syntax.py .
    cp ROS-Code/src/run-file.py .
    ```

    Batch/Cmd/Powershell
    ```bat
    copy ROS-Code/src/syntax.py .
    copy ROS-Code/src/run-file.py .
    ```

!!! example "Remove the unneeded folder"
    Shell/Terminal
    ```sh
    rm -f -r -d ROS-Code
    ```

    Batch/Cmd/Powershell
    ```bat
    rmdir /s /q ROS-Code
    ```



### As a one-liner

Shell/Terminal
```sh
git clone https://github.com/Richienb/ROS-Code.git ; cd ROS-Code ; pip install -r requirements.txt ; cd .. ; mv $PWD/ROS-Code/src/syntax.py $PWD/ROS-Code/src/ros.py ; cp ROS-Code/src/syntax.py . ; cp ROS-Code/src/run-file.py . ; rm -f -r -d ROS-Code
```

Powershell
```bat
git clone https://github.com/Richienb/ROS-Code.git ; cd ROS-Code ; pip install -r requirements.txt ; cd .. ; rename /ROS-Code/src/syntax.py ros.py ; copy ROS-Code/src/syntax.py . ; copy ROS-Code/src/run-file.py . ; rmdir /s /q ROS-Code
```

Batch/Cmd
```bat
git clone https://github.com/Richienb/ROS-Code.git & cd ROS-Code & pip install -r requirements.txt & cd .. & rename /ROS-Code/src/syntax.py ros.py & copy ROS-Code/src/syntax.py . & copy ROS-Code/src/run-file.py . & rmdir /s /q ROS-Code
```

### Using make

!!! warning "Compatibility"
    Make is only preinstalled in Linux. On other operating systems, `make` needs to be manually installed.
    For Windows, I recommend using [Chocolatey](https://chocolatey.org) and running the following command:
    ```bat
    choco install make
    ```

!!! example "Install ROS Code"
    ```sh
    make install
    ```

!!! example "Uninstall ROS Code"
    ```sh
    make uninstall
    ```

### Usage

Ensure that the `syntax.py` and `run-file.py` file are stored in the same directory.

Call the following command to execute a ROS Code file, replacing `mycode.ros` with the code you wish to run

```sh
python run-file.py mycode.ros
```

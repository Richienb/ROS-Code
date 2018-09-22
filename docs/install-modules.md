# Install ROS Code as an importable module

!!! warning "Requirements"
    Installing ROS Code using the methods described in this documentation requires Python and Pip.

ROS Code can be easily installed via the Pip CLI or from the `requirements.txt` file.

## Pip CLI

```sh
pip install ros-code-modules
```

## requirements.txt

```
ros-code-modules
```

## Custom versions

For both of the examples above, you can specify the [version](https://pypi.org/project/ros-code-modules/#history) to install right after the name.

### Exact version

Install an exact version (in this example: 2.0.0.24)

```
ros-code-modules==2.0.0.24
```

### Version between specific range

Install a version between a specific range depending on other modules using the same dependencies (in this example: 2.0.0.20 - 2.0.0.24)

```
ros-code-modules>=2.0.0.20,<2.0.0.24
```

### Version later than

Install a version later than or equal to a specific version (in this example 2.0.0.22)

```
ros-code-modules>=2.0.0.22
```

## Upgrading

To upgrade the package, run the following command in your command line

```sh
pip install --upgrade ros-code-modules
```

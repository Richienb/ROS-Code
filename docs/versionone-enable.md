# Enable ROS Code

___
### Normal Method

```python
import ros
ros.message_print('Hello World')
```

___
### Don't use the `ros` prefix

```python
from ros import *
message_print('Hello World')
```

___
### Enable only a *specific* command

```python
from ros import message_print
message_print('Hello World')
```
___
### Use a *different* command prefix other than `ros`

```python
import ros as tools
tools.message_print('Hello World')
```
___
### Enable only a *specific* command and *rename* it

```python
from ros import message_print as message
message('Hello World')
```

___

# Enable ROS Code

* * *

### Normal Method

```python
import ros
ros.message_print('Hello World')
```

* * *

### Don't use the `ros` prefix

```python
from ros import *
message_print('Hello World')
```

* * *

### Enable only a _specific_ command

```python
from ros import message_print
message_print('Hello World')
```

* * *

### Use a _different_ command prefix other than `ros`

```python
import ros as tools
tools.message_print('Hello World')
```

* * *

### Enable only a _specific_ command and _rename_ it

```python
from ros import message_print as message
message('Hello World')
```

* * *

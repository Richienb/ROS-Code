# Packages Used By ROS Code

The following list outlines all the packages used by ROS Code - useful if building from source.

Ensure you already have Python 3.x installed on your system along with Pip as the runtime doesn't have pip installer by default.

```bat
:: Install A Package
:: Replace dir_to_runtime with the directory to the runtime site-packages folder - for example: C:\ROS-Code\runtime\win\Lib\site-packages
pip install PACKAGE_NAME --target dir_to_runtime
```

??? done "Preinstalled with Python"
    subprocess
    os
    sys
    secrets
    warnings
    keyword
    importlib
    string
    textwrap
    pprint
    math
    operator
    statistics
    webbrowser
    urllib
    random
    datetime
    time
    calendar
    
???+ help "Installation may be required"
    pip

???+ warning "Installation required"
    ??? summary "Clipboard"
        `pip install clipboard'

    ??? summary "Colour"
        `pip install colour`

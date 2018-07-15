# Edit the ROS Code documentation

### Preparing

In order to edit the documentation, you will need:

-   An installation of Python 3.
-   Pip to install the required packages.

```bat
:: Install required packages using Pip
pip install mkdocs mkdocs-material pymdown-extensions Pygments
```

After installing mkdocs, start a local server in order to view your changes live.

```bat
:: Navigate to the main repository directory
cd C:\ROS-Code
:: Start the mkdocs local server
mkdocs serve
```

Now you can navigate to the URL shown in the terminal (usually [127.0.0.1:8000](http://127.0.0.1:8000)) and you will be able to see the documentation live as you edit it.

### Building

!!! done "Automatic Building"
    The documentation in the master branch will automatically be built via [Travis CI](https://travis-ci.org/Richienb/ROS-Code) if the build succeeds so manually deploying to Github Pages is not needed.

!!! note "More Information"
    Read the [mkdocs documentation](https://www.mkdocs.org) for more information.

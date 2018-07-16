# Packages Used By ROS Code

The following list outlines all the packages used by ROS Code - useful if building from source.

!!! tip "Prerequisites"
    - Python 3.x or later (Also backwards compatible with Python 2.x)
    - Pip (Refer to the [Pip Documentation](https://pip.pypa.io/en/stable/installing/))

## Executing code

One line install:
`pip install clipboard colour`

??? summary "Clipboard"
    The clipboard package allows access to the clipboard to perform related actions.
    `pip install clipboard`

??? summary "Colour"
    The colour package includes support colour based operations.
    `pip install colour`
        
### Also required for code execution

???+ summary "Future"
    The future package allows backwards compatibility with Python 2.x but is also required in Python 3.x to prevent module not found exceptions
    `pip install future`

> The following packages and steps are already automated in the consistient integration service when pushing to a branch

## Building documentation

One line install:
`mkdocs mkdocs-material pymdown-extensions Pygments`

??? summary "Mkdocs"
    The mkdocs package is the core tool for building the documentation.
    `pip install mkdocs`

??? summary "Mkdocs Material"
    The mkdocs material package is a addon for mkdocs which enables a Material Design theme.
    `pip install mkdocs-material`

??? summary "Pymdown Extensions"
    Pymdown extensions is a package which adds a number of markdown plugins.
    `pip install pymdown-extensions`

??? summary "Pygments"
    Pygments is also a package providing markdown plugins.
    `pip install pygments`
        
## Code checking

One line install:
`pip install flake8 pylint`
    
??? summary "Flake8"
    Flake8 is a package which checks code against the Flake8 specification
    `pip install flake8`
        
??? summary "Pylint"
    Pylint is another package, like Flake8 which checks code againt the Pep8 specification
    `pip install pylint`
        
## Automatic code optimisation and fixing

One line install:
`pip install autopep8 autoflake`

??? summary "Autopep8"
    The package Autopep8 optimises what it can to work with the Pep8 specification
    
??? summary "Autoflake"
    The package Autoflake optimises what it can to work with the Flake8 specification
    
> This step is automised in the consistient integration service when pushing to a branch

## Python environment and Pipfile generator

???+ summary "Pipenv"
    Pipenv is a Python environment and Pipfile generator. It creates a virtual environment to run the code in and generates a Pipfile and Pipfile.lock for usage in the future.

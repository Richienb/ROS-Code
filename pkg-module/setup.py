# Import setuptools module
import setuptools

# Parse the readme markdown file
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="ros-code-modules",
    version="2.0.0.16",
    author="Richie Bendall",
    author_email="richiebendall@gmail.com",
    description=
    "A Python module/library containing lots of tools to simplify Python development.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Richienb/ROS-Code",
    packages=setuptools.find_packages(),
    install_requires=['clipboard', 'colour', 'loremipsum'],
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
)

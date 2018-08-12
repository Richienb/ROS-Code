# Import setuptools module
import setuptools

# Import requirements parser module
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

# Parse the readme markdown file
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

# parse_requirements() returns generator of pip.req.InstallRequirement objects
INSTALL_REQS = parse_requirements('requirements.txt', session='hack')

# REQS is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
REQS = [str(ir.req) for ir in INSTALL_REQS]

setuptools.setup(
    name="ROS-Code-Module-Only",
    version="2.0.0-pre.6",
    author="Richie Bendall",
    author_email="richiebendall@gmail.com",
    description=
    "A Python module/library containing lots of tools to simplify Python development.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Richienb/ROS-Code",
    packages=setuptools.find_packages(),
    install_requires=REQS,
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

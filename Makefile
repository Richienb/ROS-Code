# If code is run with no parameters
# Prepare ROS Code
prepare:
	rm -rf -- ROS-Code
	rm -rf -- ros
	rm -f -- run_file.py
	git clone https://github.com/Richienb/ROS-Code.git
	cd ROS-Code
	pip install -r requirements.txt
	cd ..
	cp -r ./ROS-Code/src/ros ./ros
	cp ROS-Code/src/run_file.py ./run_file.py
	rm -f -r -d ROS-Code
# Uninstall ROS Code
uninstall:
	rm -rf -- ros
	rm -f -- run_file.py
# Run unit tests
utest:
	pip install autopep8 autoflake pylint flake8
	cd src
	autopep8 -i -r -a -a -a .
	autoflake .
	python test_syntax.py
	pylint .
	flake8 .

# Minimal makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = ROSCode
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

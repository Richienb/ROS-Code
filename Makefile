# If code is run with no parameters
# Prepare ROS Code
prepare:
	rm -rf -- ROS-Code 2> /dev/null
	rm -rf -- ros 2> /dev/null
	rm -f -- run_file.py 2> /dev/null
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

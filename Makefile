# If code is run with no parameters
# Prepare ROS Code
prepare:
	rm -rf -- ROS-Code
	rm -f -- ros.py
	rm -f -- run_file.py
	git clone https://github.com/Richienb/ROS-Code.git
	cd ROS-Code
	pip install -r requirements.txt
	cd ..
	mv ./ROS-Code/src/syntax.py ./ROS-Code/src/ros.py
	cp ROS-Code/src/syntax.py .
	cp ROS-Code/src/run_file.py .
	rm -f -r -d ROS-Code
# Uninstall ROS Code
uninstall:
	rm -f -- ros.py
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

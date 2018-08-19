# If code is run with no parameters
# Prepare ROS Code
prepare:
	rm -rf INSTALL-ROS-Code || true
	rm -rf ros || true
	rm -f run_file.py || true
	git clone https://github.com/Richienb/ROS-Code.git INSTALL-ROS-Code
	cd INSTALL-ROS-Code
	pip install -r requirements.txt
	cd ..
	cp -r ./INSTALL-ROS-Code/min/ros ./ros
	cp INSTALL-ROS-Code/min/run_file.py ./run_file.py
	rm -rf INSTALL-ROS-Code

# Uninstall ROS Code
uninstall:
	rm -rf ros || true
	rm -f run_file.py || true

# Run unit tests
utest:
	pip install autopep8 autoflake pylint flake8
	cd src
	autopep8 -i -r -a -a -a .
	autoflake .
	python test_syntax.py
	pylint .
	flake8 .

# Prepare ROS Code
install:
	git clone https://github.com/Richienb/ROS-Code.git
	cd ROS-Code
	pip install -r requirements.txt
	cd .. ; cp ROS-Code/src/syntax.py .
	cp ROS-Code/src/run-file.py .
	rmdir
# Uninstall ROS Code
uninstall:
	rm syntax.py
	rm run-file.py

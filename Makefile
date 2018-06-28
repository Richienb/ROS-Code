# Prepare ROS Code
install:
	git clone https://github.com/Richienb/ROS-Code.git
	cd ROS-Code
	pip install -r requirements.txt
	cd .. ; cp ROS-Code/src/syntax.py .
	cp ROS-Code/src/run-file.py .
	rmdir ROS-Code
# Uninstall ROS Code
uninstall:
	rm syntax.py
	rm run-file.py
# Install main Pip packages
pipmain: mainmodules.txt
	pip install -r mainmodules.txt
# Install main mkdocs packages
pipmkdocs:
	pip install mkdocs mkdocs-material pymdown-extensions Pygments

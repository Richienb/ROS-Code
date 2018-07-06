java -jar jython-installer.jar --silent --directory runtime --type minimum --include mod --verbose
pip install -r requirements.txt --target "$PWD\runtime\Lib\site-packages"
curl -L -o jython-installer.jar https://search.maven.org/remotecontent?filepath=org/python/jython-installer/2.7.0/jython-installer-2.7.0.jar

mkdir python-source
curl -L -o python-source.tgz https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
tar -xvzf ./python-source.tgz -C ./python-source
cd $TRAVIS_BUILD_DIR/python-source/Python-3.7.0
./configure --prefix=$TRAVIS_BUILD_DIR/python-compiled "Configuring Build..." > /dev/null
make && make install
cd $TRAVIS_BUILD_DIR
pip install -r requirements.txt --target "$TRAVIS_BUILD_DIR/python-compiled/Lib/site-packages"

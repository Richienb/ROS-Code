autopep8 --verbose --in-place --recursive --aggressive --aggressive --aggressive $PWD
autoflake --in-place --recursive $PWD
rm -f Pipfile
rm -f Pipfile.lock
pipenv install

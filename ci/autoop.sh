autopep8 --verbose --in-place --recursive --aggressive --aggressive --aggressive $PWD
autoflake --in-place --recursive $PWD
pipenv install

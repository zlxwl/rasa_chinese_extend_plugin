#! /bin/bash
rm -rf dist/*

python setup.py sdist upload

python setup.py bist_wheel upload

twine upload dist/*


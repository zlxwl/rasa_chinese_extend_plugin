#! /bin/bash
rm -rf dist/*

python setup.py sdist upload

python setup.py bdist_wheel upload

twine upload dist/*


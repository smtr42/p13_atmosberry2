#!/bin/sh

echo "Running Black"
black --line-length=79 .
echo "Running DocFormatter"
docformatter --recursive --in-place .
# echo "Running isort"
# isort --profile=black . 
echo "Running Flake8"
flake8

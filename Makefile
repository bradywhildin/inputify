PYTHON = python3

all: setup test

setup:
	pip install -r requirements.txt

test:
	${PYTHON} -m unittest discover
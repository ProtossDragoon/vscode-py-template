PROJECT = project

all: install lint test format

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

uninstall:
	python3 -m pip install --upgrade pip
	python3 -m pip uninstall -r requirements.txt

lint:
	python3 -m pylint --rcfile=pylintrc ./${PROJECT}

test:
	python3 -m unittest discover -s ./${PROJECT} -p "*_test.py" -v
	python3 -m unittest discover -s ./${PROJECT} -p "test_*.py" -v

format:
	python3 -m yapf -ir .
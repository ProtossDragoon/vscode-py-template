PROJECT = myproject

all: install-dev lint test format

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install flit
	flit install

install-dev:
	python3 -m pip install --upgrade pip
	# Install with flit
	python3 -m pip install flit
	flit install --symlink --only-deps --deps all
	# If you want to Use pip, use:
	# python3 -m pip install --require-virtualenv -e .[dev]

install-dev-without-venv:
	python3 -m pip install --upgrade pip
	# Install with flit
	python3 -m pip install flit
	flit install --symlink --only-deps --deps all
	# If you want to Use pip, use:
	# python3 -m pip install -e .[dev]

uninstall:
	python3 -m pip install --upgrade pip
	python3 -m pip uninstall ${PROJECT}

format:
	python3 -m yapf -ir .

test:
	python3 -m unittest discover -s ${PROJECT} -p "*_test.py" -v
	python3 -m unittest discover -s tests -p "*_test.py" -v
	python3 -m unittest discover -s ${PROJECT} -p "test_*.py" -v
	python3 -m unittest discover -s tests -p "test_*.py" -v

publish:
	python3 -m flit publish

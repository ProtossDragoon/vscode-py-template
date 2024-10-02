PROJECT = myproject

all: install-dev test

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install flit
	FLIT_ROOT_INSTALL=1 flit install

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

publish:
	python3 -m flit publish

test:
	@echo "Running tests in ${PROJECT}"
	@python3 -m unittest discover -s tests -p "test_*.py" -v

PROJECT_NAME:=$(shell basename $(CURDIR))

test:
	@echo $(PROJECT_NAME)

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install --upgrade setuptools wheel
	python3 setup.py sdist bdist_wheel
	pip3 install dist/*.whl
	rm -rf build dist *.egg-info

uninstall:
	pip3 uninstall -y $(PROJECT_NAME)

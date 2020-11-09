.PHONY: test init
.DEFAULT_GOAL: test

venv:
	virtualenv -p /usr/bin/python3.6 .venv

init:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest test\ -v

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
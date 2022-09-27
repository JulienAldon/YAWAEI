PYTHON = pipenv run python

.DEFAULT: usage

usage:
		@echo "Usage:"
		@echo "    make build           # Build source distribution archives"
		@echo "    make deploy_prod     # Upload source distribution archives to pypi.org"
		@echo "    make deploy_test     # Upload source distribution archives to test.pypi.org"

build:
		$(PYTHON) -m build --wheel
		$(PYTHON) -m build --sdist

deploy_test:
		twine upload -r pypitest dist/*

deploy_prod:
		twine upload -r pypi dist/*

.PHONY: usage deploy_prod deploy_test build
# This file is generated from sphinx-notes/template.
# You need to consider modifying the TEMPLATE or modifying THIS FILE.

LANG = en_US.UTF-8

MAKE = make
PY   = python3
RM   = rm -rf

.PHONY: docs
docs:
	$(MAKE) -C docs/

.PHONY: test
test:
	$(PY) -m unittest discover -s tests -v

.PHONY: dist
dist: pyproject.toml
	$(RM) dist/ # clean up old dist
	$(PY) -m build

.PHONY: install
install: dist
	$(PY) -m pip install --user --no-deps --force-reinstall dist/*.whl

.PHONY: upload
upload: dist
	$(PY) -m twine upload --repository pypi $</*

.PHONY: test-upload
test-upload: dist
	$(PY) -m twine upload --repository testpypi $</*

.PHONY: update-template
update-template:
	$(PY) -m cruft update

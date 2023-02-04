# This file is generated from sphinx-notes/template. DO NOT EDIT.

LANG = en_US.UTF-8

MAKE = make
PY   = python3
RM   = rm -rf

.PHONY: docs test dist install upload test-upload sync-template

docs:
	$(MAKE) -C docs/

test:
	$(PY) -m unittest discover -s tests -v

dist: pyproject.toml
	$(RM) dist/ # clean up old dist
	$(PY) -m build

install: dist
	$(PY) -m pip install --user --no-deps --force-reinstall dist/*.whl

upload: dist
	$(PY) -m twine upload --repository pypi $</*

test-upload: dist
	$(PY) -m twine upload --repository testpypi $</*

sync-template:
	./.sphinxnotes/template/update.py

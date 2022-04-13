LANG=en_US.UTF-8

MAKE = make
PY   = python3
RM   = rm -rf

.PHONY: docs
docs:
	$(RM) docs/_build
	$(MAKE) -C docs/

.PHONY: dist
dist: setup.py
	$(RM) dist/ build/ *.egg-info/
	$(PY) setup.py sdist bdist_wheel
	$(PY) -m twine check dist/*

.PHONY: upload
upload: dist/
	$(PY) -m twine upload --repository pypi $<*

.PHONY: install
install: dist
	$(PY) -m pip install --user --no-deps --force-reinstall dist/*.whl

.PHONY: test
test:
	$(PY) -m unittest -v

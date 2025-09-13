# This file is generated from sphinx-notes/cookiecutter.
# You need to consider modifying the TEMPLATE or modifying THIS FILE.

LANG = en_US.UTF-8

MAKE  = make
PY    = python3
RM    = rm -rf
GIT   = git
OPEN  = xdg-open

.PHONY: docs
docs:
	$(MAKE) -C docs/

.PHONY:
view:
	$(OPEN) docs/_build/html/index.html

.PHONY: clean
clean:
	$(MAKE) -C docs/ clean; $(RM) dist/

.PHONY: fmt
fmt:
	ruff format src/ && ruff check --fix src/

.PHONY: test
test:
	$(PY) -m unittest discover -s tests -v

################################################################################
# Distribution Package
################################################################################

# Build distribution package, for "install" or "upload".
.PHONY: dist
dist: pyproject.toml clean
	$(PY) -m build

# Install distribution package to user directory.
#
# NOTE: It may breaks your system-level packages, use at your own risk.
.PHONY: install
install: dist
	export PIP_BREAK_SYSTEM_PACKAGES=1 # required by Python 3.11+, see PEP-668
	$(PY) -m pip install --user --no-deps --force-reinstall dist/*.whl

# Publish wheel to PyPI offical server <https://pypi.org/> when you want to
# You should have a PyPI account and have PyPI token configured.
#
# See also https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives
.PHONY: upload
upload: dist
	$(PY) -m twine upload --repository pypi $</*

################################################################################
# Cookiecutter Incremental Updates
################################################################################

# Keep up to date with the latest template.
# See https://github.com/sphinx-notes/cookiecutter.
.PHONY: tmpl-update
tmpl-update:
	$(PY) -m cruft update

.PHONY: tmpl-update-done
tmpl-update-done:
	$(GIT) commit -m "chore: Update project template to sphinx-notes/cookiecutter@$(shell jq -r '.commit' .cruft.json | head -c8)"

.PHONY: apply-rej
apply-rej:
	@for rej in $$(find . -name '*.rej'); do \
		echo "applying $$rej..."; \
		wiggle --replace $${rej%.rej} $$rej; \
	done

# Detect the minimum Python versions needed to run code.
pyvermin:
	vermin --eval-annotations --target=3.12- --versions src/

# Update project version.
.PHONY: bump-version
bump-version:
	@echo -n "Please enter the version to bump: "
	@read version && $(PY) -m cruft update --variables-to-update "{ \"version\" : \"$$version\" }"

################################################################################
# CUSTOM TARGETS
################################################################################

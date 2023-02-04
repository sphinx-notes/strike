#!/usr/bin/env python3

from os import path
import subprocess

from cookiecutter.main import cookiecutter
from github import Github


def run_shell(*args: str) -> str:
    return subprocess.run(args, capture_output=True, text=True).stdout.strip()

# Fetch meta information.
root = run_shell('git', 'rev-parse', '--show-toplevel')
repo = path.basename(root)
version = run_shell('git', 'describe', '--tags')
desc = Github().get_user('sphinx-notes').get_repo('strike').description

# assert repo == 'strike'
print(f'root: {root}')
print(f'repo: {repo}')
print(f'version: {version}')
print(f'desc: {desc}')

# Create project from the remote repository template.
# .. seealso::
#    - https://cookiecutter.readthedocs.io/en/1.7.2/cookiecutter.html#module-cookiecutter.main
#    - https://cookiecutter.readthedocs.io/en/1.7.2/advanced/injecting_context.html
cookiecutter('gh:sphinx-notes/template',
             no_input=True,
             overwrite_if_exists=True,
             output_dir=path.dirname(root),
             extra_context={
                 'name': repo,
                 'version': version,
                 'description': desc,
             })

# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('./sphinxnotes'))
import strike as proj

from setuptools import setup, find_namespace_packages

with open('doc/index.rst') as f:
    long_desc = f.read()

setup(
    name=proj.__title__,
    version=proj.__version__,
    url=proj.__url__,
    download_url='https://pypi.org/project/' + proj.__package__.replace('-', '.'),
    license=proj.__license__,
    author=proj.__author__,
    description=proj.__description__,
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Text Processing :: Markup :: reStructuredText',
    ],
    keywords=proj.__keywords__,
    platforms='any',
    python_requires='>=3',
    packages=find_namespace_packages(include=['sphinxnotes.*']),
    include_package_data=True,
    install_requires= [
        'Sphinx',
    ],
    namespace_packages=['sphinxnotes'],
)

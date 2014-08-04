#!/usr/bin/env python

from setuptools import setup
from get_git_version import get_git_version

setup(name='tarjan',
      version=get_git_version(),
      description='Implementation of Tarjan\'s algorithm: resolve cyclic deps',
      author='Bas Westerbaan',
      author_email='bas@westerbaan.name',
      url='http://github.com/bwesterb/py-tarjan/',
      packages=['tarjan', 'tarjan.tests'],
      zip_safe=True,
      package_dir={'tarjan': 'src'},
      test_suite='tarjan.tests',
      classifiers = [
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
        ],
      )

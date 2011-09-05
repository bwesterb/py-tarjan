#!/usr/bin/env python

from setuptools import setup
from get_git_version import get_git_version

setup(name='tarjan',
      version=get_git_version(),
      description='Implementation of Tarjan\'s algorithm: resolve cyclic deps',
      author='Bas Westerbaan',
      author_email='bas@westerbaan.name',
      url='http://github.com/bwesterb/tarjan/',
      packages=['tarjan'],
      zip_safe=True,
      package_dir={'tarjan': 'src'},
      test_suite='tarjan.tests.suite'
      )

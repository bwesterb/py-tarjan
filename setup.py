#!/usr/bin/env python

from setuptools import setup

setup(name='tarjan',
      version='0.2.3.2',
      description='Implementation of Tarjan\'s algorithm: resolve cyclic deps',
      long_description='{0:s}\n{1:s}'.format(
          open('README.rst').read(),
          open('CHANGES.rst').read()),
      author='Bas Westerbaan',
      author_email='bas@westerbaan.name',
      url='http://github.com/bwesterb/py-tarjan/',
      packages=['tarjan', 'tarjan.tests'],
      zip_safe=True,
      package_dir={'tarjan': 'src'},
      test_suite='tarjan.tests',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          ],
      )

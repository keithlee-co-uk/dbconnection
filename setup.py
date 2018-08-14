#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup

with open('requirements/prod.txt') as f:
    requirements = f.read().splitlines()

setup(name='dbconnection',
      version='0.0.1',
      description='Python Database Wrapper Utility',
      author='Keith Lee',
      author_email='code@keithlee.co.uk',
      url='https://github.com/keithlee-co-uk/dbconnection',
      packages=['dbconnection'],

      install_requires=requirements,
      extras_require={
          'test': ["pytest"],
      }
      )

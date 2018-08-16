#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup

setup(name='dbconnection',
      version='0.0.2',
      description='Python Database Wrapper Utility',
      author='Keith Lee',
      author_email='code@keithlee.co.uk',
      url='https://github.com/keithlee-co-uk/dbconnection',

      install_requires=['mysql-connector'],
      extras_require={
          'test': ["pytest"],
      }
      )

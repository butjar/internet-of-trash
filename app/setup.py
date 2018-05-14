#!/usr/bin/env python

from distutils.core import setup

setup(name='app',
      scripts=['app/subscriber/subscriber.py'],
      version='0.1.0',
      description='',
      author='Martin Fleischer',
      author_email='martin.fleischer@studio.unibo.it',
      url='',
      packages=['app', 'app.jobs', 'app.subscriber', 'app.worker'],
     )

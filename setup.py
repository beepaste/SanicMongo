# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def get_version_from_file():
    # get version number from __init__ file
    # before module is installed

    fname = 'SanicMongo/__init__.py'
    with open(fname) as f:
        fcontent = f.readlines()
    version_line = [l for l in fcontent if 'VERSION' in l][0]
    return version_line.split('=')[1].strip().strip("'").strip('"')


def get_long_description_from_file():
    # content of README will be the long description

    fname = 'README'
    with open(fname) as f:
        fcontent = f.read()
    return fcontent

VERSION = get_version_from_file()
DESCRIPTION = """
MongoMotor: An async document-object mapper for MongoDB
"""
LONG_DESCRIPTION = get_long_description_from_file()

setup(name='SanicMongo',
      version=VERSION,
      author='BeePaste',
      author_email='hi@beepaste.io',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      url='http://mongomotor.poraodojuca.net/',
      packages=find_packages(exclude=['tests', 'tests.*']),
      install_requires=['mongoengine>=0.10', 'motor>=1.1', 'blinker>=1.3',
                        'pymongo<4,>=3.4', 'greenlet==0.4.5'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      test_suite='tests',
      provides=['SanicMongo'])

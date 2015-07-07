#!/usr/bin/env python

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='steamspy',
    version='0.0.1',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    license='MIT',
    description='Steamspy api wrapper lib.',
    long_description=README,
    url='https://github.com/fly/steamspy',
    author='Jon Chen',
    author_email='bsd@voltaire.sh',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=[
        'requests==2.7.0',
    ],
    extras_require={
        'docs': [
            'sphinx==1.3.1',
        ],
    },
)

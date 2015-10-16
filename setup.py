#!/usr/bin/env python

from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='rockin-refbox',
    version='0.1',
    description='The RoCKIn referee box',
    long_description=readme(),
    packages=['protobuf_comm', 'msgs', 'examples', 'tests'],
    package_dir={
        'protobuf_comm': 'src/libs/protobuf_comm',
        'msgs': 'rockin/msgs',
        'examples': 'rockin/examples',
        'tests': 'src/libs/protobuf_comm/tests',
    },
    install_requires=[
        'tornado',
    ],
    test_suite='tests',
    tests_require=['pytest'],
)

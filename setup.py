#!/bin/env python

import setuptools

params = dict(
    name='micro-server',
    description='A micro server',
    author='Tristan',
    author_email='tdecacqu@redhat.com',
    packages=['micro', 'micro.server'],
    entry_points={'console_scripts': ['micro-server = micro.server.cmd:run']},
)


__name__ == '__main__' and setuptools.setup(**params)

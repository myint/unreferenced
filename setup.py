#!/usr/bin/env python
"""Setup for unreferenced."""

import ast
from distutils import core


def version():
    """Return version string."""
    with open('unreferenced.py') as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s


with open('README.rst') as readme:
    core.setup(name='unreferenced',
               version=version(),
               description='Reports unreferenced files.',
               long_description=readme.read(),
               license='Expat License',
               author='Steven Myint',
               url='https://github.com/myint/unreferenced',
               classifiers=['Intended Audience :: Developers',
                            'Environment :: Console',
                            'Programming Language :: Python :: 2.6',
                            'Programming Language :: Python :: 2.7',
                            'Programming Language :: Python :: 3',
                            'License :: OSI Approved :: MIT License'],
               keywords='unreferenced, files, clean',
               py_modules=['unreferenced'],
               scripts=['unreferenced'])

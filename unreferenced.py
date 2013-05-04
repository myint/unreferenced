"""Finds unreferenced files.

These files are reported as candidates for removal.

"""

__version__ = '0.1.1'


import argparse
import os
import subprocess


IGNORE_EXTENSIONS = [
    '.gcov',
    '.pyc',
    '~'
]


def grep(text, path):
    """Return True if text is found in path.

    Do a recursive search if path is a directory.

    """
    return 0 == subprocess.call(['grep', '--quiet', '--recursive', text, path])


def ignore(filename):
    """Return True if we should ignore filename."""
    if filename.startswith('.'):
        return True

    for extension in IGNORE_EXTENSIONS:
        if filename.endswith(extension):
            return True

    return False


def unreferenced_files(path):
    """Yield names of unreferenced files in path.

    Completely ignore hidden directories when recursing directories.

    """
    for root, directories, filenames in os.walk(path):
        for name in filenames:
            if ignore(name):
                continue

            if name.endswith('.py'):
                if grep(name.rsplit('.', 1)[0], path):
                    continue
            else:
                if grep(name, path):
                    continue

            yield os.path.join(root, name)

        directories[:] = [d for d in directories if not d.startswith('.')]


def main():
    """Entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='+')
    args = parser.parse_args()

    for filename in args.paths:
        for name in unreferenced_files(filename):
            print(name)

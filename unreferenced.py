"""Finds unreferenced files.

These files are reported as candidates for removal.

"""

import argparse
import os
import subprocess


def grep(text, path):
    """Return True if text is found in path.

    Do a recursive search if path is a directory.

    """
    return 0 == subprocess.call(['grep', '--quiet', '--recursive', text, path])


def unreferenced_files(path):
    """Yield names of unreferenced files in path.

    Completely ignore hidden directories when recursing directories.

    """
    for _, directories, filenames in os.walk(path):
        for name in filenames:
            if name.endswith('.py'):
                if grep(name.rsplit('.', 1)[0], path):
                    continue
            else:
                if grep(name, path):
                    continue

            yield name

        directories[:] = [d for d in directories if not d.startswith('.')]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='+')
    args = parser.parse_args()

    for filename in args.paths:
        for name in unreferenced_files(filename):
            print(name)

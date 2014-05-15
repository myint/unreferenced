"""Finds unreferenced files.

These files are reported as candidates for removal.

"""

__version__ = '0.1.5'


import argparse
import os
import subprocess


IGNORE_EXTENSIONS = [
    '.a',
    '.dylib',
    '.gcov',
    '.o',
    '.pyc',
    '.so',
    '~'
]


def grep(text, path, exclude):
    """Return True if text is found in path.

    Do a recursive search if path is a directory.

    """
    # Do recursion in Python so we can ignore hidden directories (in a
    # cross-platform manner).
    for root, directories, filenames in os.walk(path):
        for name in filenames:
            if 0 == subprocess.call(['grep',
                                     '--quiet',
                                     '--recursive',
                                     '--binary-files=without-match'] +
                                    ['--exclude=' + x
                                     for x in exclude] +
                                    [text,
                                     os.path.join(root, name)]):
                return True

        directories[:] = [d for d in directories if not d.startswith('.')]

    return False


def ignore(filename):
    """Return True if we should ignore filename."""
    if filename.startswith('.'):
        return True

    for extension in IGNORE_EXTENSIONS:
        if filename.endswith(extension):
            return True

    return False


def unreferenced_files(path, exclude_referrers):
    """Yield names of unreferenced files in path.

    Completely ignore hidden directories when recursing directories.

    """
    _grep = lambda x: grep(x,
                           path,
                           exclude=exclude_referrers + [os.path.join(path, x)])

    for root, directories, filenames in os.walk(path):
        for name in filenames:
            if ignore(name):
                continue

            if name.endswith('.py'):
                if _grep(name.rsplit('.', 1)[0]):
                    continue
            elif name.endswith('.java'):
                if _grep(name.rsplit('.', 1)[0]):
                    continue
            else:
                if _grep(name):
                    continue

            yield os.path.join(root, name)

        directories[:] = [d for d in directories if not d.startswith('.')]


def main():
    """Return nonzero error code if unreferenced files are found."""
    parser = argparse.ArgumentParser()
    parser.add_argument('directories', nargs='+')
    parser.add_argument('--exclude-referrers', default='',
                        help='comma-separated list of files to exclude as '
                             'referrers')
    args = parser.parse_args()

    total = 0
    for filename in args.directories:
        for name in unreferenced_files(
                filename,
                exclude_referrers=args.exclude_referrers.split(',')):
            print(name)
            total += 1

    return 2 if total else 0

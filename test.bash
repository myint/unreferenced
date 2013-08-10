#!/bin/bash -ex
#
# Minimal test.

rm -rf ./.test
mkdir -p ./.test
touch ./.test/unused.txt
echo 'self_reference' > ./.test/self_reference
touch ./.test/okay.txt
echo 'okay.txt' > ./.test/referrer.txt
[ $(./unreferenced ./.test | wc -l) -eq 3 ]
rm -rf ./.test

echo -e '\x1b[01;32mOK\x1b[0m'

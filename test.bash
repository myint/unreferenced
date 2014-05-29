#!/bin/bash -eux
#
# Minimal test.

rm -rf ./.test
mkdir -p ./.test
touch ./.test/unused.txt
echo 'self_reference' > ./.test/self_reference
touch ./.test/okay.txt
echo 'okay.txt' > ./.test/referrer.txt
readonly LINES=$(./unreferenced ./.test | wc -l)
[ "$LINES" -eq 3 ]
rm -rf ./.test

echo -e '\x1b[01;32mOK\x1b[0m'

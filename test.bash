#!/bin/bash -eux
#
# Minimal test.

trap "echo -e '\x1b[01;31mFailed\x1b[0m'" ERR

rm -rf ./.test
mkdir -p ./.test
touch ./.test/unused.txt
echo 'self_reference' > ./.test/self_reference
touch ./.test/okay.txt
echo 'okay.txt' > ./.test/referrer.txt
readonly lines=$(./unreferenced ./.test | wc -l)
[ "$lines" -eq 3 ]
rm -rf ./.test

echo -e '\x1b[01;32mOkay\x1b[0m'

#!/usr/bin/env bash

cd tests/snapshots/output

for f in *$1*;
do
    echo $f
    diff $f ../validation/$f || (vimdiff $f ../validation/$f && sleep 1)
done

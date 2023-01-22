#!/usr/bin/env bash

dir1=$1
dir2=$2
echo "First directory:  $dir1"
echo "Second directory: $dir2"

/usr/bin/python3 main.py --dir1=$dir1 --dir2=$dir2 | grep 'Only\|Differing'

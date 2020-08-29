#!/bin/bash

set -eu

if [ $# -ne 1 ]; then
  echo 'This script extracts the highest rated movies.'
  echo 'Usage: '${0}' <inputfile_path>'
  exit 1
fi

cat ${1} | grep -e '4\..*点' -e '5\..*点' | cut -d, -f1 >MOVIE.txt

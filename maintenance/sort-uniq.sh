#/bin/bash

set -eu

if [ $# -ne 1 ]; then
  echo '# Removes duplicate lines after sorting the input file.'
  echo 'Usage: ./'${0}' <inputfile_path>'
  exit 1
fi

sort ${1} | uniq | tee ${1}

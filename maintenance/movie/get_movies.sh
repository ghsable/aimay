#!/bin/bash

set -eu

read -p "Do you make a lot of requests to Filmarks? (y/n) :" YN
if [ "${YN}" = "y" ]; then
  # 2020/08/29: 1..92440
  for i in {18438..92440}
  do
    echo https://filmarks.com/movies/${i},$(curl -fsL https://filmarks.com/movies/${i} \
    | grep -oP '<title>.*点' | sed 's/<title>//g' | sed -E 's/ - 映画.*★/,/g; s/ - 映画.*平均スコア：/,/g')
  done >>$(date "+%Y%m%d")_MOVIES.txt
else
  exit 1;
fi


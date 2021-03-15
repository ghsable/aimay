#!/bin/bash

# --- Maintain a page with a different structure.
#cat YYYYMMDD_MOVIES.txt | grep '点' >tenari
#cat YYYYMMDD_MOVIES.txt | grep -v '点' >tennashi
#cat tennashi | tr -d ',' >tennashi_urls

#sh ./test.sh
while read url
  do
    echo ${url},$(curl -fsL ${url} \
    | grep -e '<title>.*</title>' -e '平均スコア' | tr '\n\r' ' ' | grep -oP '.*点' | sed -E 's/.*<title>//g; s/ - 映画.*★/,/g; s/ - 映画.*平均スコア：/,/g')
  done <tennashi_urls >>tennashi_fix

#cat tenari tennashi_fix | sort -V >tenarinashi
#rm tenari tennashi tennashi_urls tennashi_fix YYYYMMDD_MOVIES.txt
#mv tenarinashi YYYYMMDD_MOVIES.txt

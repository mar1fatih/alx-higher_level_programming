#!/usr/bin/env bash
# script count the url request body lines
url=$1
curl -s $url | wc -c

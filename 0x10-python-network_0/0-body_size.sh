#!/bin/bash
# script count the url request body lines
curl -s $1 | wc -c

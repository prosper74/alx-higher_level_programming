#!/bin/bash
# Script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
# Requirement:
#   The size must be displayed in bytes
#   You have to use curl

curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '

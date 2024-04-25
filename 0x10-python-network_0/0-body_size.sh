#!/bin/bash
# Script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
# Requirement:
#   The size must be displayed in bytes
#   You have to use curl

curl -s "$1" | wc -c
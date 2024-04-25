#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -o /dev/null -w '%{http_code}' -sLI "$1"

#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -X PUT -s 0.0.0.0:5000/catch_me --output /dev/null --header "Content-Type: text/plain" --data "You got me!"

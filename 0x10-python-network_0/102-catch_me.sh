#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -X PUT -s 0.0.0.0:5000/catch_me --output /dev/null --header "Content-Type: text/plain" --data "You got me!"
curl -sL -X PUT -H "You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me

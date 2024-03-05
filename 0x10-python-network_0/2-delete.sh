#!/bin/bash
# Sends a DELETE request to a server and displays the respose body of the response

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

#getting the url
url=$1

curl -s -X DELETE -o response.txt "$url"
cat response.txt

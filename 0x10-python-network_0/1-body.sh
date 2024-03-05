#!/bin/bash
#sends a GET rquest to a url and prints out the response body

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

status_code=$(curl -s -w "%{http_code}" -o response.txt "$url")

if [ "$status_code" -eq 200 ]; then
    cat response.txt
else
    echo "status code not 200"
fi

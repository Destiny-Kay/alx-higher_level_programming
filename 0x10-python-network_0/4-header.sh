#!/bin/bash
#Sends a GET request to the url and sets a header to it

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

response=$(curl -s -X GET -H "X-School-User-Id: 98" "$url")
echo "$response"

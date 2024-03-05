#!/bin/bash
# Returns all methos a url accepts

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

methods_allowed=$(curl -s -i -X OPTIONS "$url" | grep -i Allow | sed 's/Allow: //i')
echo "$methods_allowed"

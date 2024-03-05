#!/bin/bash
#bash script that returns the size of body in bytes

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
response=$(curl -s -w "%{size_download}" -o /dev/null "$url")
echo "$response"

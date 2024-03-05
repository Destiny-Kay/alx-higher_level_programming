#!/bin/bash
#bash script that returns the size of body in bytes
response=$(curl -s -w "%{size_download}" -o /dev/null "$1") && echo "$response"

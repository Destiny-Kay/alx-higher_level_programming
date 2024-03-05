#!/bin/bash
#Sends a GET request to the url and sets a header to it
response=$(curl -s -X GET -H "X-School-User-Id: 98" "$1") && echo "$response"

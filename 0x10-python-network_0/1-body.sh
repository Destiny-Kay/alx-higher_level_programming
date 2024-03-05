#!/bin/bash
#sends a GET rquest to a url and prints out the response body
status_code=$(curl -s -w "%{http_code}" -o response.txt "$1") && [ "$status_code" -eq 200 ] && cat response.txt

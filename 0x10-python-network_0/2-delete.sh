#!/bin/bash
# Sends a DELETE request to a server and displays the respose body of the response
curl -s -X DELETE -o response.txt "$1" && cat response.txt

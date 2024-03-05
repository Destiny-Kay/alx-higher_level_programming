#!/bin/bash
#Sends a GET request to the url and sets a header to it
curl -sH "X-School-User-Id: 98" "${1}"

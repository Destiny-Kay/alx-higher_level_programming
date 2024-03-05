#!/bin/bash
# Returns all methos a url accepts
curl -Is "$1" | grep -i "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev

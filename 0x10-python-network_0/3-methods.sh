#!/bin/bash
# Returns all methos a url accepts
methods_allowed=$(curl -s -i -X OPTIONS "$1" | grep -i Allow | sed 's/Allow: //i') && echo "$methods_allowed"

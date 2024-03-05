#!/bin/bash
# Sends a POST request and displays response body. sets some params
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"

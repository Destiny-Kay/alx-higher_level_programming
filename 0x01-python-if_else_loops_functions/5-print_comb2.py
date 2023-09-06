#!/usr/bin/python3
# 5-print_comb.py

"""Prints number combinations"""

for i in range (100):
    if i == 99:
        print(f"{i}")
    else:
        print(f"{i:02}, ", end="")
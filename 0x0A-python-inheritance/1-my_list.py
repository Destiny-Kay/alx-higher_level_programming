#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    Prints a sorted list using the built-in list class.
    """

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

#!/usr/bin/python3

if __name__ == "__main__":
    """Adds all arguments provided"""
    import sys
    arg_count = sys.argv
    sum_total = 0
    for i in range(len(arg_count) - 1):
        sum_total += int(sys.argv[i + 1])
    print(f"{sum_total}")

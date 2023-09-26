#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''a function that prints x elements of a list'''
    num = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num += 1
        except IndexError:
            break
    print("")
    return (num)

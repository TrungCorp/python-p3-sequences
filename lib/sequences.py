#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    for k in range(length):
        if k == 0:
            fib_list.append(0)
        elif k== 1:
            fib_list.append(1)
        else:
            new_num = fib_list[-2] +fib_list[-1]
            fib_list.append(new_num)
    print(fib_list)


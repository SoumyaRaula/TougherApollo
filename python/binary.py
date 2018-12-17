#!/bin/python3

import math
import os
import random
import re
import sys

list_of_binary = []

def check_counter(lista):
    dummy_list = []
    actual_list = []
    max_count = 0
    for i in lista:
        if i == 1:
            dummy_list.append(i)
        if i == 0:
            if dummy_list:
                actual_list.append(dummy_list)
            dummy_list = []
            continue
    else:
        actual_list.append(dummy_list)
    
    if actual_list:
        max_count = max([len(x) for x in actual_list])
    return max_count
        
def binary_check(n):
    if n >= 1:
        list_of_binary.append(n%2)
        binary_check(n//2)
    return (list_of_binary[::-1])

if __name__ == '__main__':
    n = int(input())
    lista = binary_check(n)
    sys.stdout.write(str(check_counter(lista)))

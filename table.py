#! python3
# -*- coding: utf-8 -*-

first = int(input())
second = int(input())
third = int(input())
fourth = int(input())

if first > second or third >fourth:
    print("Fuck you")
elif first > 10 or second > 10 or third > 10 or fourth > 10:
    print("Fuck you")
else:
    for x in range(third, fourth+1):
        print('\t', x, end="")
    print()
    for foo in range(first, second+1):
        print(foo, end='\t')
        for egg in range(third, fourth+1):
            print(foo * egg, end='\t')
        print()
print()

#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    if n < 3:
        print(0)
    else:
        a1 = 1
        a2 = 2
        evenNumberSum = a2
        while a1+a2 < n:
            a3 = a1 + a2
            if a3 % 2 == 0:
                evenNumberSum += a3
            a1 = a2
            a2 = a3
        print(evenNumberSum)
        
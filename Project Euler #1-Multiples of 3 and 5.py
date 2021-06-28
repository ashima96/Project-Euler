#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    n3 = (n-1)//3
    s3 = n3 * (n3 + 1)*3//2
    
    n5 = (n-1)//5
    s5 = n5 * (n5 + 1)*5//2
    
    n15 = (n-1)//15
    s15 = n15 * (n15 + 1)*15//2
    
    print(s3 + s5 - s15)
    
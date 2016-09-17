#!/bin/python
#Python 2
import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

arr.reverse() 
print " ".join(str(x) for x in arr)

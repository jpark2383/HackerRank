#Python 2
import sys
from collections import deque

word = raw_input()
result = word
res = []

for letter in word:
    if res and res[-1] == letter:
        res.pop()
    else:
        res.append(letter)
if res:
    print "".join(res)
else:
    print "Empty String"
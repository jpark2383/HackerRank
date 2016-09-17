#Python 2
#!/bin/python

import sys


s = raw_input().strip()
count = 1
for letter in s:
    if letter.isupper():
        count = count + 1

print count
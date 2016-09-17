import math
n = int(raw_input())
printed = 0
for x in xrange (n):
    S = raw_input()
    R = S[::-1]
    for ch in xrange(1, len(S)):
        if (abs(ord(S[ch]) - ord(S[ch-1])) != abs(ord(R[ch]) - ord(R[ch-1]))):
            print "Not Funny"
            printed = 1
            break
    if not printed:
        print "Funny"
    printed = 0
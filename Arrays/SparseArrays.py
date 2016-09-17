import sys

n = int(input().strip())
words = {}
for x in range(n):
    word = input().strip()
    if word not in words.keys():
        words[word] = 1
    else:
        words[word] += 1
Q = int(input().strip())
for i in range(Q):
    check = input().strip()
    if check in words.keys():
        print(words[check])
    else:
        print("0")
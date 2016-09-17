#Python 2

word = raw_input().lower()
flag = 1
letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
           'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
          's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
for letter in word:
    if letter in letters.keys():
        letters[letter] = 1

for value in letters.values():
    if value == 0:
        flag = 0
if flag:
    print "pangram"
else:
    print "not pangram"
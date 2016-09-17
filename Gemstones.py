# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
eles = {}
count = 0
for gem in range (0, n):
    rock = str(raw_input().strip())
    for ch in rock:
        if ch not in eles.keys():
            eles[ch] = 1
        elif eles[ch] == gem:
            eles[ch] += 1
    for val in eles.values():
        if val == n:
            count += 1
print count
# Enter your code here. Read input from STDIN. Print output to STDOUT
#Python 2

n, d = map(int, raw_input().strip().split())
arr = list(map(int, raw_input().strip().split()))

d %= n
print " ".join(str(x) for x in arr[d:]) + " " + " ".join(str(y) for y in arr[:d])
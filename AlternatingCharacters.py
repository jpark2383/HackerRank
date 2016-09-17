# Python 2
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
check = ""
count = 0
for x in range (0, n):
    word = str(raw_input().strip())
    if word[0] == "A":
        check = "B"
    else:    
        check = "A"
    for ch in range(1, len(word)):
        if check == "B":
            if word[ch] != check:
                count = count + 1
            else:
                check = "A"
        elif check == "A":
            if word[ch] != check:
                count = count + 1
            else:
                check = "B"
    print count
    count = 0
        
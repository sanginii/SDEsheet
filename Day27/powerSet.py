s = 'abc'
n = len(s)
for i in range(2**n):
    substring = ''
    for j in range(n):
        if (i & (1<<j)):
            substring+=s[j]
    print (substring)
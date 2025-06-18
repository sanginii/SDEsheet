n=4
s = "11"  # start from n=2
for i in range(3, n+1):  # loop runs n - 2 times
    t = ""
    s += "&"  # sentinel to avoid index out of range
    c = 1
    for j in range(1, len(s)):  # inner loop depends on len(s)
        if s[j] != s[j-1]:
            t += str(c) + s[j-1]
            c = 1
        else:
            c += 1
    s = t  # next string becomes current

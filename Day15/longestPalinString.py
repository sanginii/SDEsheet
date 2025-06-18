def longestPalindrome(s):
    n = len(s)
    start = 0
    max_len = 1

    for i in range(n):
        # Odd length
        l, r = i, i #centre position
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1
        
        # Even length
        l, r = i, i+1
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1

    return s[start:start+max_len]

print(longestPalindrome("aabb"))

def longestCommonPrefix(strs): 
    if not strs:
        return ""

    for i in range(len(strs[0])):  # Loop over first string
        char = strs[0][i]
        for s in strs[1:]:         # Compare with rest
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    
    return strs[0]
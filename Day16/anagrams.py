from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list) # mapping charCount to List of Anagrams
    for st in strs:
        count = [0] * 26 # a
        for c in st:
            count [ord (c) - ord ("a") ] += 1
        res[tuple(count)].append(st)
    return list(res.values())

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    return all(c == 0 for c in count)

def wordBreak(s, wordDict):
    def canBreak(start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and canBreak(end):
                return True
        return False
    
    return canBreak(0)

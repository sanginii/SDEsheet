res = []
path = []
s = "aabb"
def partitionHelper(index: int):
    if index == len(s):
        res.append(path[:])
        return 
    for i in range(index, len(s)):
        if isPalindrome(s, index, i):
            path.append(s[index:i + 1])
            partitionHelper(i + 1)
            path.pop()

def isPalindrome(s: str, start: int, end: int) -> bool:
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

partitionHelper(0)
print (res) 
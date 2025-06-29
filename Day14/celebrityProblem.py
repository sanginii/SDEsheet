def findCelebrity(M):
    n = len(M)
    
    def knows(a, b):
        return M[a][b] == 1

    # Step 1: Find a candidate
    celeb = 0
    for i in range(1, n):
        if knows(celeb, i):
            celeb = i

    # Step 2: Verify candidate
    for i in range(n):
        if i != celeb:
            if knows(celeb, i) or not knows(i, celeb):
                return -1
    return celeb

#stack method
def findCelebrity(M):
    n = len(M)
    
    def knows(a, b):
        return M[a][b] == 1

    stack = [i for i in range(n)]

    # Eliminate until one candidate remains
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        if knows(a, b):
            stack.append(b)  # a can't be celeb
        else:
            stack.append(a)  # b can't be celeb

    if not stack:
        return -1  # No candidate

    celeb = stack.pop()

    # Verify
    for i in range(n):
        if i != celeb:
            if knows(celeb, i) or not knows(i, celeb):
                return -1
    return celeb

def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    d = 256             # number of characters in input alphabet
    q = 101             # a prime number for modulo
    h = pow(d, m-1) % q # d^(m-1) % q

    p_hash = 0  # hash of pattern
    t_hash = 0  # hash of current window in text

    result = []

    # Initial hash for pattern and first window
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide the pattern over text
    for i in range(n - m + 1):
        # If hash matches, check characters one by one
        if p_hash == t_hash:
            if text[i:i+m] == pattern:
                result.append(i)

        # Compute hash for next window
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q  # Make sure it's positive

    return result

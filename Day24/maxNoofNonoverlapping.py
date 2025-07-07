def maxNumOfSubstrings(s: str):
    n = len(s)
    first = {}
    last = {}

    # Step 1: Record first and last index of each character
    for i, c in enumerate(s):
        first[c] = min(first.get(c, i), i)
        last[c] = max(last.get(c, i), i)

    # Step 2: Expand the interval to find minimal valid substring
    def get_valid_substring(start):
        end = last[s[start]]
        i = start
        while i <= end:
            if first[s[i]] < start:
                return None  # invalid interval
            end = max(end, last[s[i]])
            i += 1
        return (start, end)

    # Step 3: Collect all valid minimal substrings
    intervals = []
    for i in range(n):
        if i == first[s[i]]:
            interval = get_valid_substring(i)
            if interval:
                intervals.append(interval)

    # Step 4: Sort by end index and greedily select non-overlapping substrings
    intervals.sort(key=lambda x: x[1])
    res = []
    prev_end = -1

    for start, end in intervals:
        if start > prev_end:
            res.append(s[start:end + 1])
            prev_end = end

    return res

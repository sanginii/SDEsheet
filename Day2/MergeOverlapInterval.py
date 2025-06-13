intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort(key = lambda x:x[0])
merged = [intervals[0]]

for curr in intervals[1:]:
    last = merged[-1]
    if curr[0]<=last[1]:
        last[1] = max(last[1],curr[1])
    else:
        merged.append(curr)
print (merged)
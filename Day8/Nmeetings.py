N = 6
start = [1,3,0,5,8,5]
end   = [2,4,5,7,9,9]

# Sort by end time
meetings = sorted(zip(start, end, range(N)), key=lambda x: x[1])

res = []
last_end = 0
for s, e, idx in meetings:
    if s >= last_end:
        res.append(idx + 1)  # 1-based index if required
        last_end = e

print("Meeting order:", res)

        
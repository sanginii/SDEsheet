g = [1,2,3], s = [1,1]
s.sort()
g.sort()
i=j=count=0
while i < len(g) and j < len(s):
    if s[j]>=g[i]:
        count+=1
        i+=1
        j+=1
    else:
        j+=1
print (count) 
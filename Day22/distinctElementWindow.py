from collections import defaultdict
a = [1,2,2,1,3,1,1,3]
k = 4
def distinctEleWindow(a, k, ans):
    freq = defaultdict(int)
    i=j=0
    while i <= len(a)-k:
        freq[a[j]]+=1
        if j >= i+k-1:
            ans.append(len(freq))
            freq[a[i]]-=1
            if freq[a[i]]==0:
                del freq[a[i]]
            i+=1
        j+=1
ans = []
distinctEleWindow(a, k, ans)
print(ans) 
#time - O(elements) worst case k=0, dict lookups O(1) and to calulate length? and to del?
#space - ans O(k) to store the answer dictonary to store disctinct elements in a window worst case O(k) incase all k elements are distinct 
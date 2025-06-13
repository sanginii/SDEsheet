#bruteforce 
a = [-1,0,1,2,-1,-1]  
n=len(a)
ans = set()
for i in range (n):
    for j in range (i+1,n):
        for k in range (j+1,n):
            if a[i]+a[j]+a[k]==0:
                triplet = tuple(sorted([a[i],a[j],a[k]]))
                ans.add(triplet)
print(ans) 

#better
def triplet(n, arr):
    st = set()
    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            # Calculate the 3rd element:
            third = -(arr[i] + arr[j])
            # Find the element in the set:
            if third in hashset:
                temp = [arr[i], arr[j], third]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(arr[j])
    # store the set in the answer:
    ans = list(st)
    return ans
arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
ans = triplet(n, arr)
print(ans)

#optimal 
def triplet(n, arr):
    ans = []
    arr.sort()
    for i in range(n):
        # remove duplicates:
        if i != 0 and arr[i] == arr[i - 1]:
            continue
        # moving 2 pointers:
        j = i + 1
        k = n - 1
        while j < k:
            total_sum = arr[i] + arr[j] + arr[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)
                j += 1
                k -= 1
                # skip the duplicates:
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1
    return ans




#only a tuple can be added to set
# lst = [] 
# lst.append(4)
# tpl = (1, 2, "hi") Tuples can’t be changed
# s = set()  
# s = {1, 2, 3}
# s.add(4) 
# s.add((1, 2)) a tuple is fine no list or set
# d = {}
# d["city"] = "Chennai"
# d[(1, 2)] = "ok" 

# we can convert 
# | From → To              | Possible? | Example                                         |
# | ---------------------- | --------- | ----------------------------------------------- |
# | List → Set             | ✅ Yes     | `set([1, 2, 2]) → {1, 2}`                       |
# | List → Tuple           | ✅ Yes     | `tuple([1, 2, 3]) → (1, 2, 3)`                  |
# | Tuple → List           | ✅ Yes     | `list((1, 2, 3)) → [1, 2, 3]`                   |
# | Set → List             | ✅ Yes     | `list({1, 2, 3}) → [1, 2, 3]`                   |
# | Set → Tuple            | ✅ Yes     | `tuple({1, 2, 3}) → (1, 2, 3)`                  |
# | List of pairs → Dict   | ✅ Yes     | `dict([("a", 1), ("b", 2)]) → {"a": 1, "b": 2}` |
# | Dict → List of keys    | ✅ Yes     | `list({"a": 1, "b": 2}) → ["a", "b"]`           |
# | Dict → List of items   | ✅ Yes     | `list(dict.items()) → [("a", 1), ("b", 2)]`     |
# | Dict Keys/Values → Set | ✅ Yes     | `set(dict.keys())`, `set(dict.values())`        |

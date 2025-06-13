a = [3, 8, 5, 7, 6]
ele = set(a)
mx=0

for i in ele:
    if i-1 not in ele:
        j=i
        cnt=1
        while j+1 in ele:
            cnt+=1
            j+=1 
        mx = max(mx,cnt) 
print(mx) 

#for set insertion O(1) in best and average and O(N) in worst when collisions happen rare case
#the second for loop is 2N not N^2 because once we checked for 1 we are not doing it again for 2,3,4 

#always remain the thing we are doing again and again always that is optemized either result stored or something like that
#space complexity for set O(N)
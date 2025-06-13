#bruteforce
a=[7,1,5,3,6,4]
max_profit=0
for i in range (len(a)):
    for j in range (i+1,len(a)):
        profit=a[j]-a[i]
        max_profit = max(max_profit,profit)
print(max_profit) 


#Optimal
min=float("inf")
max_profit=float("-inf")
profit = 0
for i in range (len(a)):
    if a[i]<min:
        min = a[i]
    profit = a[i]-min
    max_profit=max(profit,max_profit)
print(max_profit) 

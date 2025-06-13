class job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit
jobs = [job(1, 4, 20), job(2, 1, 10), job(3, 2, 40), job(4, 2, 30)]
jobs.sort(key=lambda x: x.profit, reverse=True) 
# {(3,1,40),(4,1,30),(1,4,20),(2,1,10)}

#finding maximum deadline
maxi = jobs[0].deadline 
for i in range(1, len(jobs)): 
    maxi = max(maxi, jobs[i].deadline)

#array will be of maximum deadline length 
slot = [-1] * (maxi + 1)
countJobs = 0
jobProfit = 0

for i in range(len(jobs)): 
    for j in range(jobs[i].deadline, 0, -1): 
        if slot[j] == -1:
            slot[j] = i
            countJobs += 1
            jobProfit += jobs[i].profit
            break
print (countJobs, jobProfit) 
#time O(NlogN)+O(N*M) 
#space O(M)
#Optimized Approach Using DSU
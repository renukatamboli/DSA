class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        jobs = sorted(Jobs, key = lambda x:x.profit, reverse=True)
        maxi = 0
        profit = 0
        total = 0
        arr = set()
        for job in jobs:
            for i in range(job.deadline,0,-1):
                if i not in arr:
                    arr.add(i)
                    profit += job.profit
                    total += 1
                    break
        return [total,profit]

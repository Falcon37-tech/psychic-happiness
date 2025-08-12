Today's Problem is -

You are given two arrays: deadline[], and profit[], which represent a set of jobs, where each job is associated with a deadline, and a profit. Each job takes 1 unit of time to complete, and only one job can be scheduled at a time. You will earn the profit associated with a job only if it is completed by its deadline.

Your task is to find:

The maximum number of jobs that can be completed within their deadlines.
The total maximum profit earned by completing those jobs.
Examples :

Input: deadline[] = [4, 1, 1, 1], profit[] = [20, 10, 40, 30]
Output: [2, 60]
Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40).
Input: deadline[] = [2, 1, 2, 1, 1], profit[] = [100, 19, 27, 25, 15]
Output: [2, 127]
Explanation: Job1 and Job3 can be done with maximum profit of 127 (100+27).
Input: deadline[] = [3, 1, 2, 2], profit[] = [50, 10, 20, 30]
Output: [3, 100]
Explanation: Job1, Job3 and Job4 can be completed with a maximum profit of 100 (50 + 20 + 30).
Constraints:
1 ≤ deadline.size() == profit.size() ≤ 10^5
1 ≤ deadline[i] ≤ deadline.size()
1 ≤ profit[i] ≤ 500

Solution
Code-
class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        jobs = list(zip(deadline, profit))
        jobs.sort(key = lambda x: -x[1])
        maxdeadline = max(deadline)
        
        parent = [i for i in range(maxdeadline + 1)]
        
        def find(slot):
            if parent[slot] != slot:
                parent[slot] = find(parent[slot])
            return parent[slot]
            
        def merge(u, v):
            parent[u] = v
            
        count = 0
        maxprofit = 0
        
        for d, p in jobs:
            availableslot = find(d)
            if availableslot > 0:
                merge(availableslot, availableslot - 1)
                count += 1
                maxprofit += p
        return [count, maxprofit]

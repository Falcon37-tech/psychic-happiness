Today's Problem is-

Given an array of integers cost[] where cost[i] is the cost of the ith step on a staircase. Once the cost is paid, you can either climb one or two steps. Return the minimum cost to reach the top of the floor.
Assume 0-based Indexing. You can either start from the step with index 0, or the step with index 1.

Examples:

Input: cost[] = [10, 15, 20]
Output: 15
Explanation: Cheapest option is to start at cost[1], pay that cost, and go to the top.



Input: cost[] = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest option is to start on cost[0], and only step on 1s, skipping cost[3].


Constraints:
2 ≤ cost.size() ≤ 10^5
0 ≤ cost[i] ≤ 999

Solution
Code-

#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0]*(n+1)
        for i in range(2, n+1):
            dp[i] = min(
                dp[i-1] + cost[i-1],
                dp[i-2] + cost[i-2]
                )
        return dp[n]

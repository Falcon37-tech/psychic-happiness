Today's Problem is -

There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Your task is to count the number of ways, the person can reach the top (order does matter).

Examples:

Input: n = 1
Output: 1
Explanation: There is only one way to climb 1 stair. 
Input: n = 2
Output: 2
Explanation: There are 2 ways to reach 2th stair: {1, 1} and {2}.  
Input: n = 4
Output: 5
Explanation: There are five ways to reach 4th stair: {1, 1, 1, 1}, {1, 1, 2}, {2, 1, 1}, {1, 2, 1} and {2, 2}.
Constraints:
1 ≤ n ≤ 44

Solution
Code-

class Solution:
    def countWays(self, n):
        if n == 0 or n == 1:
            return 1
            
        ways = [0]*(n+1)
        ways[0] = 1
        ways[1] = 1
        for i in range(2, n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]

Today's Problem is-

Given an array arr[] of non-negative integers of size n. Find the maximum possible XOR between two numbers present in the array.

Examples:

Input: arr[] = [25, 10, 2, 8, 5, 3]
Output: 28
Explanation: The maximum possible XOR is 5 ^ 25 = 28.
Input: arr[] = [1, 2, 3, 4, 5, 6, 7]
Output: 7
Explanation : The maximum possible XOR is 1 ^ 6 = 7.
Constraints:
2 ≤ arr.size() ≤ 5*10^4
1 ≤ arr[i] ≤ 10^6

Soolution
Code-

class Solution:
    def maxXor(self, arr):
        maxXor = 0
        mask = 0
        
        for i in range(31, -1, -1):
            mask |= (1<<i)
            prefixes = {num & mask for num in arr}
            candidate = maxXor | (1<<i)
            if any((candidate^p) in prefixes for p in prefixes):
                maxXor = candidate
        return maxXor

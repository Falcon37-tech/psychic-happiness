Today's Problem is -

Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.

Examples:

Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
Output: 6
Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.
Input: arr[] = [0, 0, 1, 1, 0]
Output: 4
Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.
Input: arr[] = [0]
Output: 0
Explnation: There is no subarray with an equal number of 0s and 1s.
Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 1

Solution
code -

class Solution:
    def maxLen(self, arr):
        prefix_map = {0: -1}
        max_len = 0
        prefix_sum = 0
        
        for i, num in enumerate(arr):
            
            if num == 0:
                prefix_sum += -1
            else:
                prefix_sum += 1
            
            
            if prefix_sum in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum])
                
            else:
                prefix_map[prefix_sum] = i
        return max_len

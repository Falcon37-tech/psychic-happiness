Todays Problem is -

Given an unsorted array of integers, find the number of subarrays having sum exactly equal to a given number k.

Examples:

Input: arr = [10, 2, -2, -20, 10], k = -10
Output: 3
Explaination: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum exactly equal to -10.
Input: arr = [9, 4, 20, 3, 10, 5], k = 33
Output: 2
Explaination: Subarrays: arr[0...2], arr[2...4] have sum exactly equal to 33.
Input: arr = [1, 3, 5], k = 0
Output: 0
Explaination: No subarray with 0 sum.
Constraints:

1 ≤ arr.size() ≤ 105
-103 ≤ arr[i] ≤ 103
-107 ≤ k ≤ 107

Solution
Code -

class Solution:
    def countSubarrays(self, arr, k):
        prefix_sum_count = {0:1}
        count = 0
        current_sum = 0
        
        for num in arr:
            current_sum += num
            diff = current_sum - k
            count += prefix_sum_count.get(diff, 0)
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
            
        return count


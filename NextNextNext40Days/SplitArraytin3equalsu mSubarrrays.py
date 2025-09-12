Today's Problem is:

Given an array, arr[], determine if arr can be split into three consecutive parts such that the sum of each part is equal. If possible, return any index pair(i, j) in an array such that sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), otherwise return an array {-1,-1}.

Note: Since multiple answers are possible, return any of them. The driver code will print true if it is correct otherwise, it will print false.

Examples :

Input:  arr[] = [1, 3, 4, 0, 4]
Output: true
Explanation: [1, 2] is valid pair as sum of subarray arr[0..1] is equal to sum of subarray arr[2..3] and also to sum of subarray arr[4..4]. The sum is 4, so driver code prints true.
Input: arr[] = [2, 3, 4]
Output: false
Explanation: No three subarrays exist which have equal sum.
Input: arr[] = [0, 1, 1]
Output: false
Constraints:
3 ≤ arr.size() ≤ 10^6
0 ≤ arr[i] ≤ 10^6

Solution
Code-
#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        total = sum(arr)
        n = len(arr)
        
        if total % 3 != 0:
            return [-1,-1]
            
        target = total // 3
        prefix = 0
        first, second = -1, -1
        
        for i in range(n):
            prefix += arr[i]
            
            if prefix == target and first == -1:
                first = i
            elif prefix == 2*target and first != -1:
                second = i
                break
            
        if first != -1 and second != -1 and second < n - 1:
            return [first, second]
            
        return [-1,-1]


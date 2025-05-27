Today's Problem was-

Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

Examples:

Input: arr[] = [3, 0, 1, 0, 4, 0 2]
Output: 10
Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.
Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides.
Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
Output: 9
Explanation: Total water trapped = 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units.
Constraints:
1 < arr.size() < 105
0 < arr[i] < 103

Solution
Code -
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n <= 2:
            return 0
            
        left, right = 0, n - 1
        left_max = right_max = 0
        total_water = 0
        
        while left<=right:
            if arr[left] <= arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                    
                else:
                    total_water += left_max - arr[left]
                    
                left += 1
                
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    total_water += right_max - arr[right]
                right -= 1
                
        return total_water

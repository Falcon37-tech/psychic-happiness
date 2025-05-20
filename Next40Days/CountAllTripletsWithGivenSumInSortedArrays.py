Today's Problem is -

Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k.

Examples:

Input: arr[] = [-3, -1, -1, 0, 1, 2], target = -2
Output: 4
Explanation: Four triplets that add up to -2 are:
arr[0] + arr[3] + arr[4] = (-3) + 0 + (1) = -2
arr[0] + arr[1] + arr[5] = (-3) + (-1) + (2) = -2
arr[0] + arr[2] + arr[5] = (-3) + (-1) + (2) = -2
arr[1] + arr[2] + arr[3] = (-1) + (-1) + (0) = -2
Input: arr[] = [-2, 0, 1, 1, 5], target = 1
Output: 0
Explanation: There is no triplet whose sum is equal to 1. 
Constraints:
3 ≤ arr.size() ≤ 104
-105 ≤ arr[i], target ≤ 105

Solution
Code-

class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        count = 0
        
        for i in range(n - 2):
            a = arr[i]
            newtarget = target - a
            left = i + 1
            right = n - 1
            
            while left < right:
                b = arr[left]
                c = arr[right]
                total = b + c
                
                if total < newtarget:
                    left += 1
                elif total > newtarget:
                    right -= 1
                else:
                    if b == c:
                        num_element = right - left + 1
                        count += (num_element*(num_element - 1)) // 2
                        break
                    else:
                        count_b = 1
                        while left + 1 < right and arr[left] == arr[left + 1]:
                            left += 1
                            count_b += 1
                        
                        count_c = 1
                        while right - 1 > left and arr[right] == arr[right - 1]:
                            right -= 1
                            count_c += 1
                        
                        count += count_b*count_c
                        left += 1
                        right -= 1
                        
        return count

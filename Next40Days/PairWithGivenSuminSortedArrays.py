Today's Problem is - 
You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
Note: pairs should have elements of distinct indexes. 

Examples :

Input: arr[] = [-1, 1, 5, 5, 7], target = 6
Output: 3
Explanation: There are 3 pairs which sum up to 6 : {1, 5}, {1, 5} and {-1, 7}.
Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: There are 6 pairs which sum up to 2 : {1, 1}, {1, 1}, {1, 1}, {1, 1}, {1, 1} and {1, 1}.
Input: arr[] = [-1, 10, 10, 12, 15], target = 125
Output: 0
Explanation: There is no such pair which sums up to 125.
Constraints:
-105 <= target <=105
 2 <= arr.size() <= 105
-105 <= arr[i] <= 105
Solution
Code=
class Solution:
    def countPairs (self, arr, target) : 
        n = len(arr)
        left, right = 0, n-1
        count = 0
        
        while left < right:
            s = arr[left] + arr[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
                
            else:
                if arr[left] == arr[right]:
                    num = right - left + 1
                    count += (num*(num - 1)) // 2
                    break
                else:
                    countLeft = 1
                    countRight = 1
                    while left + 1 < right  and arr[left] == arr[left + 1]:
                        countLeft += 1
                        left += 1
                    while right - 1 > left  and arr[right] == arr[right - 1]:
                        countRight += 1
                        right -= 1
                    count += countLeft*countRight
                    left += 1
                    right -= 1
        return count

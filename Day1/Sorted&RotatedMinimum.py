Todays problem is - 
A sorted array of distinct elements arr[] is rotated at some unknown point, the task is to find the minimum element in it.

Input: arr[] = [5, 6, 1, 2, 3, 4]
Output: 1
Explanation: 1 is the minimum element in the array.
Input: arr[] = [3, 1, 2]
Output: 1
Explanation: Here 1 is the minimum element.
Input: arr[] = [4, 2, 3]
Output: 2
Explanation: Here 2 is the minimum element.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 109

Solution

Code -
#User function Template for python3

class Solution:
    def findMin(self, arr):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            
            if arr[low] <= arr[high]:
                return arr[low]
                
            mid = (low+high) // 2
            next_ = (mid + 1) % len(arr)
            prev = (mid -1 + len(arr)) % len(arr)
            
            if arr[mid] <= arr[next_] and arr[mid] <= arr[prev]:
                return arr[mid]
            
            if arr[mid] >= arr[low]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

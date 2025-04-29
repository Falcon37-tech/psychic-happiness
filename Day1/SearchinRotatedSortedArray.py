Todays Problem is -

Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key. Return -1 if the key is not found.

Examples :

Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
Output: 8
Explanation: 3 is found at index 8.
Input: arr[] = [3, 5, 1, 2], key = 6
Output: -1
Explanation: There is no element that has value 6.
Input: arr[] = [33, 42, 72, 99], key = 42
Output: 1
Explanation: 42 is found at index 1.
Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 106
1 ≤ key ≤ 106

Solution
Code -

#User function Template for python3

class Solution:
    def search(self,arr,key):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == key:
                return mid
            
            if arr[left] <= arr[mid]:
                if arr[left] <= key < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                
            else:
                if arr[mid] < key <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

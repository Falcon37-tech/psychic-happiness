Today's problem is -

Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist). If there are multiple peak elements, return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

Note: Consider the element before the first element and the element after the last element to be negative infinity.

Examples :

Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].
Input: arr = [10, 20, 15, 2, 23, 90, 80]
Output: true
Explanation: arr[1] = 20 and arr[5] = 90 are peak elements because arr[0] < arr[1] > arr[2] and arr[4] < arr[5] > arr[6]. 
Input: arr = [1, 2, 3]
Output: true
Explanation: arr[2] is a peak element because arr[1] < arr[2] and arr[2] is the last element, so it has negative infinity to its right.
Constraints:
1 ≤ arr.size() ≤ 106
-231 ≤ arr[i] ≤ 231 - 1

Solution

Code - 
##Approach 1 - Binary Search Algorithm

class Solution:   
    def peakElement(self,arr):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            left_neighbour = arr[mid - 1] if mid > 0 else float('-inf')
            right_neighbour = arr[mid + 1] if mid < len(arr) - 1 else float('-inf')
            
            if arr[mid] > left_neighbour and arr[mid] > right_neighbour:
                return mid
                
            if arr[mid] < right_neighbour:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


##Approach 2 - Brute Force Algorithm

def peakElement(arr):
    n = len(arr)

    for i in range(n):
        left = True
        right = True
        # Check for the element to the left
        if i > 0 and arr[i] <= arr[i - 1]:
            left = False
        # Check for the element to the right
        if i < n - 1 and arr[i] <= arr[i + 1]:
            right = False
        # If arr[i] is greater than its left as well as
        # the right element, return its index
        if left and right:
            return i


Today's Problem is-

Given an array arr[] of size n, filled with numbers from 1 to n-1 in random order. The array has only one repetitive element. Your task is to find the repetitive element.

Note: It is guaranteed that there is a repeating element present in the array.

Examples:

Input: arr[] = [1, 3, 2, 3, 4]
Output: 3 
Explanation: The number 3 is the only repeating element.
Input: arr[] = [1, 5, 1, 2, 3, 4]
Output: 1  
Explanation: The number 1 is the only repeating element.
Input: arr[] = [1, 1]  
Output: 1
Explanation: The array is of size 2 with both elements being 1, making 1 the repeating element.
Constraints:
2 ≤ arr.size() ≤ 10^5
1 ≤ arr[i] ≤ n-1 

Solution
Code-
class Solution:
    def findDuplicate(self, arr):
        seen = set()
        for num in arr:
            if num in seen:
                return num
            seen.add(num)

Today's Problem is-

Given a unsorted array arr[] of positive integers having all the numbers occurring exactly twice, except for one number which will occur only once. Find the number occurring only once.

Examples :

Input: arr[] = [1, 2, 1, 5, 5]
Output: 2
Explanation: Since 2 occurs once, while other numbers occur twice, 2 is the answer.
Input: arr[] = [2, 30, 2, 15, 20, 30, 15]
Output: 20
Explanation: Since 20 occurs once, while other numbers occur twice, 20 is the answer.
Constraints
1 ≤  arr.size()  ≤ 10^6
0 ≤ arr[i] ≤ 10^9

Solution
Code-
class Solution:
    def findUnique(self, arr):
        result = 0
        for num in arr:
            result ^= num
        return result

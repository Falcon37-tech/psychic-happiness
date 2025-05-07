Todays Problem is -

Given a 2D integer matrix mat[][] of size n x m, where every row and column is sorted in increasing order and a number x, the task is to find whether element x is present in the matrix.
Examples:

Input: mat[][] = [[3, 30, 38],[20, 52, 54],[35, 60, 69]], x = 62
Output: false
Explanation: 62 is not present in the matrix, so output is false.
Input: mat[][] = [[18, 21, 27],[38, 55, 67]], x = 55
Output: true
Explanation: 55 is present in the matrix.
Input: mat[][] = [[1, 2, 3],[4, 5, 6],[7, 8, 9]], x = 3
Output: true
Explanation: 3 is present in the matrix.
Constraints:
1 <= n, m <=1000
1 <= mat[i][j] <= 109
1<= x <= 109

Solution

Code - 
class Solution:
    def matSearch(self, mat, x):
	    n = len(mat)
	    m = len(mat[0])
	    
	    i, j = 0, m - 1
	    
	    while i < n and j >= 0:
	        if mat[i][j] == x:
	             return True
	        elif mat[i][j] > x:
	            j -= 1
	        else:
	            i += 1
	    return False


Today's Problem is -

You are given a two-dimensional mat[][] of size n*m containing English alphabets and a string word. Check if the word exists on the mat. The word can be constructed by using letters from adjacent cells, either horizontally or vertically. The same cell cannot be used more than once.

Examples :

Input: mat[][] = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
Output: true
Explanation:

The letter cells which are used to construct the "GEEK" are colored.
Input: mat[][] = [['T', 'E', 'U'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
Output: false
Explanation:

It is impossible to construct the string word from the mat using each cell only once.
Input: mat[][] = [['A', 'B', 'A'], ['B', 'A', 'B']], word = "AB"
Output: true
Explanation:

There are multiple ways to construct the word "AB".
Constraints:
1 ≤ n, m ≤ 6
1 ≤ L ≤ 15
mat and word consists of only lowercase and uppercase English letters.

Solution

Code-

class Solution:
	def isWordExist(self, mat, word):
		if not mat or not mat[0]:
		    return False
		    
		n, m = len(mat), len(mat[0])
		   
		def dfs(i, j, k):
		    if k == len(word):
		        return True
		    if i<0 or i>=n or j<0 or j>=m or mat[i][j] != word[k]:
		        return False
		           
		    temp = mat[i][j]
		    mat[i][j] = '#'
		       
		    found = (dfs(i+1, j, k+1) or
		             dfs(i-1, j, k+1) or
		             dfs(i, j+1, k+1) or
		             dfs(i, j-1, k+1))
		    mat[i][j] = temp
		    return found
		       
		for i in range(n):
		    for j in range(m):
		        if mat[i][j] == word[0] and dfs(i, j, 0):
		            return True
		             
		return False

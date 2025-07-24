Today's Problem is-

Given two strings s1 and s2. Return the minimum number of operations required to convert s1 to s2.
The possible operations are permitted:

Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.
Examples:

Input: s1 = "geek", s2 = "gesek"
Output: 1
Explanation: One operation is required, inserting 's' between two 'e' in s1.
Input: s1 = "gfg", s2 = "gfg"
Output: 0
Explanation: Both strings are same.
Input: s1 = "abcd", s2 = "bcfe"
Output: 3
Explanation: We can convert s1 into s2 by removing ‘a’, replacing ‘d’ with ‘f’ and inserting ‘e’ at the end. 
Constraints:
1 ≤ s1.length(), s2.length() ≤ 10^3
Both the strings are in lowercase.

Solution
Code-

class Solution:
	def editDistance(self, s1, s2):
		m, n = len(s1), len(s2)
		dp = [[0]*(n+1) for _ in range(m+1)]
		
		for i in range(m+1):
		    dp[i][0] = i
		for j in range(n+1):
		    dp[0][j] = j
		    
		for i in range(1, m+1):
		    for j in range(1, n+1):
		        
		        if s1[i-1] == s2[j-1]:
		            dp[i][j] = dp[i-1][j-1]
		        else:
		            dp[i][j] = 1 + min(
		                dp[i][j-1],
		                dp[i-1][j],
		                dp[i-1][j-1]
		            )
		                
		return dp[m][n]

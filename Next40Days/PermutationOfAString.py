Today's Problem is -

Given a string s, which may contain duplicate characters, your task is to generate and return an array of all unique permutations of the string. You can return your answer in any order.

Examples:

Input: s = "ABC"
Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
Explanation: Given string ABC has 6 unique permutations.
Input: s = "ABSG"
Output: ["ABGS", "ABSG", "AGBS", "AGSB", "ASBG", "ASGB", "BAGS", "BASG", "BGAS", "BGSA", "BSAG", "BSGA", "GABS", "GASB", "GBAS", "GBSA", "GSAB", "GSBA", "SABG", "SAGB", "SBAG", "SBGA", "SGAB", "SGBA"]
Explanation: Given string ABSG has 24 unique permutations.
Input: s = "AAA"
Output: ["AAA"]
Explanation: No other unique permutations can be formed as all the characters are same.
Constraints:
1 <= s.size() <= 9
s contains only Uppercase english alphabets

Solution

Code-
#User function Template for python3

class Solution:
    def findPermutation(self, s):
        res = []
        freq = {}
        
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
            
            
        def backtrack(path):
            if len(path) == len(s):
                res.append("".join(path))
                return
            
            for char in freq:
                if freq[char] > 0:
                    path.append(char)
                    freq[char] -= 1
                    
                    backtrack(path)
                    
                    freq[char] += 1
                    path.pop()
                    
        backtrack([])
        return res

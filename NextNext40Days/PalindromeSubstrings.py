Today's Problem is-

Given a string s, count all palindromic sub-strings present in the string. The length of the palindromic sub-string must be greater than or equal to 2.

Note: A substring is palindromic if it reads the same forwards and backwards.

Examples:

Input: s = "abaab"
Output: 3
Explanation: All palindromic substrings (of length > 1) are: "aba", "aa", "baab".
Input: s = "aaa"
Output: 3
Explanation: All palindromic substrings (of length > 1) are: "aa", "aa", "aaa".
Input: s = "abbaeae"
Output: 4
Explanation: All palindromic substrings (of length > 1) are: "bb", "abba", "aea", "eae".
Constraints:
2 ≤ s.size() ≤ 10^3
s contains only lowercase english characters

Solution
Code-

class Solution:
    def countPS(self, s):
        n = len(s)
        
        count = 0
        
        def expand(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left]==s[right]:
                if right - left + 1 >= 2:
                    count += 1
                left -= 1
                right += 1
                
        for i in range(n):
            expand(i, i)
            expand(i, i+1)
        return count

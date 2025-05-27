Todays Problem is-

Given a string s, find the length of the longest substring with all distinct characters. 

Examples:

Input: s = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest substring with all distinct characters.
Input: s = "aaa"
Output: 1
Explanation: "a" is the longest substring with all distinct characters.
Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring with all distinct characters is "abcdef", which has a length of 6.
Constraints:
1<= s.size()<=3*104
All the characters are in lowercase.

Solution
Code-

class Solution:
    def longestUniqueSubstr(self, s):
        n = len(s)
        char_index = {}
        max_len = 0
        start = 0
        
        for end in range(n):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            char_index[s[end]] = end
            max_len = max(max_len, end - start + 1)
        return max_len

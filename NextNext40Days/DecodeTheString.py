Today's Problem is -

[⚠️ Suspicious Content] Given an encoded string s, the task is to decode it. The encoding rule is :

k[encodedString], where the encodedString inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer, and encodedString contains only lowercase english alphabets.
Note: The test cases are generated so that the length of the output string will never exceed 105 .

Examples:

Input: s = "1[b]"
Output: "b"
Explanation: "b" is present only one time.
Input: s = "3[b2[ca]]"
Output: "bcacabcacabcaca"
Explanation:
1. Inner substring “2[ca]” breakdown into “caca”.
2. Now, new string becomes “3[bcaca]”
3. Similarly “3[bcaca]” becomes “bcacabcacabcaca ” which is final result.
Constraints:
1 ≤ |s| ≤ 10^5 
1 <= k <= 100

Solution
Code-
class Solution:
    def decodedString(self, s):
        stack = []
        curr_num = 0
        curr_str = ""
        
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num*10 + int(ch)
            elif ch == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + num*curr_str
            else:
                curr_str += ch
        return curr_str 

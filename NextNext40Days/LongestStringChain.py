Today's Problem is-

You are given an array of words where each word consists of lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB. For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k = 1.

Return the length of the longest possible word chain with words chosen from the given list of words in any order.

Examples:

Input: words[] = ["ba", "b", "a", "bca", "bda", "bdca"]
Output: 4
Explanation: One of the longest word chains is ["a", "ba", "bda", "bdca"].
Input: words[] = ["abc", "a", "ab"]
Output: 3
Explanation: The longest chain is {"a", "ab" "abc"}
Input: words[] = ["abcd", "dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
Constraint:
1 <= words.length <= 10^4
1 <= words[i].length <= 10
 words[i] only consists of lowercase English letters.

Solution
Code-
#User function Template for python3

class Solution:
    def longestStringChain(self, words):
        words.sort(key=len)
        
        dp = {}
        max_chain = 1
        
        for word in words:
            dp[word]=1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            max_chain = max(max_chain, dp[word])
        return max_chain

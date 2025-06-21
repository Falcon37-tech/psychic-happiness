Today's Problem is:

Given a binary tree, convert the binary tree to its Mirror tree.

Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.     

Examples:

Input: root[] = [1, 2, 3, N, N, 4]
Output: [1, 3, 2, N, 4]
Explanation: 

In the inverted tree, every non-leaf node has its left and right child interchanged.
Input: root[] = [1, 2, 3, 4, 5]
Output: [1, 3, 2, N, N, 5, 4]
Explanation:

In the inverted tree, every non-leaf node has its left and right child interchanged.
Constraints:
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^5

Solution
Code-

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        if root is None:
            return
            
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)

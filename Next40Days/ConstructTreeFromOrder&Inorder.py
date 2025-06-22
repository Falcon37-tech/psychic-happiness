Today's Problem is -

Given two arrays representing the inorder and preorder traversals of a binary tree, construct the tree and return the root node of the constructed tree.

Note: The output is written in postorder traversal.

Examples:

Input: inorder[] = [1, 6, 8, 7], preorder[] = [1, 6, 7, 8]
Output: [8, 7, 6, 1]
Explanation: The tree will look like

Input: inorder[] = [3, 1, 4, 0, 2, 5], preorder[] = [0, 1, 3, 4, 2, 5]
Output: [3, 4, 1, 5, 2, 0]
Explanation: The tree will look like

Input: inorder[] = [2, 5, 4, 1, 3], preorder[] = [1, 4, 5, 2, 3]
Output: [2, 5, 4, 3, 1]
Explanation: The tree will look like

Constraints:
1 ≤ number of nodes ≤ 10^3
0 ≤ nodes -> data ≤ 10^3
Both the inorder and preorder arrays contain unique values.

Solution

Code-
'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTreeRec(self, l, h, preorder, mp, index):
        if l>h:
            return None
            
        value = preorder[index[0]]
        root = Node(value)
        index[0] += 1
        
        root.left = self.buildTreeRec(l, mp[value]-1, preorder, mp, index)
        root.right = self.buildTreeRec(mp[value]+1,  h, preorder, mp, index)
        
        return root
        
    def buildTree(self, inorder, preorder):
        index = [0]
        
        n = len(inorder)
        mp = {}
        
        for i in range(n):
            mp[inorder[i]]=i
            
        root = self.buildTreeRec(0, n-1, preorder, mp, index)
        
        return root

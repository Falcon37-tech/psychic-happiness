Today's Problem is-

Given a Binary Search Tree (with all values unique) and two nodes n1 and n2 (n1 != n2). You may assume that both nodes exist in the tree. Find the Lowest Common Ancestor (LCA) of the given two nodes in the BST.

LCA between two nodes n1 and n2 is defined as the lowest node that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).

Examples:

Input: root = [5, 4, 6, 3, N, N, 7, N, N, N, 8], n1 = 7, n2 = 8
        
Output: 7
Explanation: 7 is the closest node to both 7 and 8, which is also an ancestor of both the nodes.
Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], n1 = 8, n2 = 14
                
Output: 8
Explanation: 8 is the closest node to both 8 and 14, which is also an ancestor of both the nodes.
Input: root = [2, 1, 3], n1 = 1, n2 = 3
        
Output: 2
Explanation: 2 is the closest node to both 1 and 3, which is also an ancestor of both the nodes.
Constraints:
1 <= number of nodes <= 10^5
1 <= node->data <= 10^5
1 <= n1, n2 <= 10^5

Solution

Code-

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def LCA(self, root, n1, n2):
        
        v1 = n1.data if isinstance(n1, Node) else n1
        v2 = n2.data if isinstance(n2, Node) else n2
        
        if root is None:
            return None
            
        if v1 < root.data and v2 < root.data:
            return self.LCA(root.left, v1, v2)
            
        if v1 > root.data and v2 > root.data:
            return self.LCA(root.right, v1, v2)
            
        return root

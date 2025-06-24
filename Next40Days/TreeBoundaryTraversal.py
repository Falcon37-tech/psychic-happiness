Today's Problem is-

Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left Boundary: This includes all the nodes on the path from the root to the leftmost leaf node. You must prefer the left child over the right child when traversing. Do not include leaf nodes in this section.

Leaf Nodes: All leaf nodes, in left-to-right order, that are not part of the left or right boundary.

Reverse Right Boundary: This includes all the nodes on the path from the rightmost leaf node to the root, traversed in reverse order. You must prefer the right child over the left child when traversing. Do not include the root in this section if it was already included in the left boundary.

Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 

Examples:

Input: root[] = [1, 2, 3, 4, 5, 6, 7, N, N, 8, 9, N, N, N, N]
Output: [1, 2, 4, 8, 9, 6, 7, 3]
Explanation:
 
Input: root[] = [1, 2, N, 4, 9, 6, 5, N, 3, N, N, N, N 7, 8]
Output: [1, 2, 4, 6, 5, 7, 8]
Explanation:
            
As the root doesn't have a right subtree, the right boundary is not included in the traversal.
Input: root[] = [1, N, 2, N, 3, N, 4, N, N] 
Output: [1, 4, 3, 2]
Explanation:

Left boundary: [1] (as there is no left subtree)
Leaf nodes: [4]
Right boundary: [3, 2] (in reverse order)
Final traversal: [1, 4, 3, 2]
Constraints:
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^5

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
    def isLeaf(self, node):
        return node.left is None and node.right is None
        
    def addLeftBoundary(self, node, res):
        curr = node.left
        while curr:
            if not self.isLeaf(curr):
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    def addLeaves(self, node, res):
        if node is None:
            return
        if self.isLeaf(node):
            res.append(node.data)
            return
        if node.left:
            self.addLeaves(node.left, res)
        if node.right:
            self.addLeaves(node.right, res)
    def addRightBoundary(self, node, res):
        curr = node.right
        temp = []
        while curr:
            if not self.isLeaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        res.extend(reversed(temp))
    def boundaryTraversal(self, root):
        if not root:
            return []
        res = []
        if not self.isLeaf(root):
            res.append(root.data)
        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addRightBoundary(root, res)
        return res

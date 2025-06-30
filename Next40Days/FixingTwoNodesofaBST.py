Today's Problem is -

Given the root of a Binary search tree(BST), where exactly two nodes were swapped by mistake. Your task is to fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
Note: It is guaranteed that the given input will form BST, except for 2 nodes that will be wrong. All changes must be reflected in the original Binary search tree(BST).
 
Examples :
Input: root = [10, 5, 8, 2, 20]
     
Output:
Explanation: The nodes 20 and 8 were swapped. 

--------------------------------------------
Input: root = [5, 10, 20, 2, 8]
     
Output:
     
Explanation: The nodes 10 and 5 were swapped.
--------------------------------------------

Constraints:
1 ≤ Number of nodes ≤ 10^3

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
    def __init__(self):
        self.first = None
        self.middle = None
        self.last = None
        self.prev = Node(float('-inf'))
        
    def correctBST(self, root):
        self.inorder(root)
        
        if self.first and self.last:
            self.first.data, self.last.data = self.last.data, self.first.data
            
        elif self.first and self.middle:
            self.first.data, self.middle.data = self.middle.data, self.first.data
        return root
        
    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        if self.prev and root.data < self.prev.data:
            
            if not self.first:
                self.first = self.prev
                self.middle = root
            else:
                self.last = root
                
        self.prev = root
        self.inorder(root.right)

Today's Problem is-

Given a Binary Search Tree(BST) and a target. Check whether there's a pair of Nodes in the BST with value summing up to the target. 

Examples:

Input: root = [7, 3, 8, 2, 4, N, 9], target = 12
       bst
Output: True
Explanation: In the binary tree above, there are two nodes (8 and 4) that add up to 12.
Input: root = [9, 5, 10, 2, 6, N, 12], target = 23
          bst-3
Output: False
Explanation: In the binary tree above, there are no such two nodes exists that add up to 23.
Constraints:

1 ≤ Number of Nodes ≤ 10^5
1 ≤ target ≤ 10^6

Solution
Code-

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    def findTarget(self, root, target): 
        def inorder(node,vals):
            if not node:
                return
            inorder(node.left, vals)
            vals.append(node.data)
            inorder(node.right, vals)
            
        vals = []
        inorder(root, vals)
        
        left, right = 0, len(vals) - 1
        while left<right:
            current_sum = vals[left] + vals[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return False

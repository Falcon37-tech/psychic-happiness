Today's Problem is -

Given a binary tree, the diameter (also known as the width) is defined as the number of edges on the longest path between two leaf nodes in the tree. This path may or may not pass through the root. Your task is to find the diameter of the tree.

Examples:

Input: root[] = [1, 2, 3]

Output: 2
Explanation: The longest path has 2 edges (node 2 -> node 1 -> node 3).

Input: root[] = [5, 8, 6, 3, 7, 9]

Output: 4
Explanation: The longest path has 4 edges (node 3 -> node 8 -> node 5 -> node 6 -> node 9).

Constraints:
1 ≤ number of nodes ≤ 10^5
0 ≤ node->data ≤ 10^5

Solution
Code -

from collections import deque
'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def diameter(self, root):
        self.max_diameter = 0
        
        def height(node):
            if not node:
                return 0
                
            left_height = height(node.left)
            right_height = height(node.right)
                
            current_diameter = left_height + right_height
                
            self.max_diameter = max(self.max_diameter, current_diameter)
                
            return 1 + max(left_height, right_height)
                
        height(root)
        return self.max_diameter

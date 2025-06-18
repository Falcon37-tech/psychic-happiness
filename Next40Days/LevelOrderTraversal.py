Today'r Problem is -

Given a root of a binary tree with n nodes, the task is to find its level order traversal. Level order traversal of a tree is breadth-first traversal for the tree.

Examples:

Input: root[] = [1, 2, 3]

Output: [[1], [2, 3]]
Input: root[] = [10, 20, 30, 40, 50]

Output: [[10], [20, 30], [40, 50]]
Input: root[] = [1, 3, 2, N, N, N, 4, 6, 5]

Output: [[1], [3, 2], [4], [6, 5]]
Constraints:

1 ≤ number of nodes ≤ 10^5
0 ≤ node->data ≤ 10^9

Solution

Code-

from collections import deque

"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
class Solution:
    def buildTree(self, root):
        if not arr or arr[0] == 'N':
            return None
        root = Node(int(arr[0]))
        q = deque([root])
        i = 1
        while q and i < len(arr):
            current = q.popleft()
            if arr[i] != 'N':
                current.left = Node(int(arr[i]))
                q.append(current.left)
            i += 1
            if i >= len(arr):
                break
            if arr[i] != 'N':
                current.right = Node(int(arr[i]))
                q.append(current.right)
            i += 1
        return root
    def levelOrder(self, root):
        if not root:
            return[]
        result = []
        q = deque([root])
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result

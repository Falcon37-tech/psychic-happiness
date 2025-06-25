Today's Problem is -

Given a binary tree, the task is to find the maximum path sum. The path may start and end at any node in the tree.

Examples:

Input: root[] = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4]
Output: 42
Explanation: 

Max path sum is represented using green colour nodes in the above binary tree.
Input: root[] = [-17, 11, 4, 20, -2, 10]
Output: 31
Explanation: 

Max path sum is represented using green colour nodes in the above binary tree.
Constraints:
1 ≤ number of nodes ≤ 10^3
-104 ≤ node->data ≤ 10^4

Solution
Code-
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        self.max_sum = float('-inf')
        def max_gain(node):
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            current_path_sum = node.data + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path_sum)
            return node.data + max(left_gain, right_gain)
        max_gain(root)
        return self.max_sum
def buildTree(s):
    if not s or s[0] == "N":
            return None
    ip = s.strip().split()
    root = Node(int(ip[0]))
    q = [root]
    i = 1
    while q and i < len(ip):
        curr = q.pop(0)
        if i < len(ip) and ip[i] != "N":
            curr.right = Node(int(ip[0]))
            q.append(curr.right)
        i+=1
    return root

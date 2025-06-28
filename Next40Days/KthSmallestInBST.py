Today's Problem is -
Given a BST and an integer k, the task is to find the kth smallest element in the BST. If there is no kth smallest element present then return -1.

Examples:

Input: root = [2, 1, 3], k = 2
    
Output: 2
Explanation: 2 is the 2nd smallest element in the BST.
Input: root = [2, 1, 3], k = 5
    
Output: -1
Explanation: There is no 5th smallest element in the BST as the size of BST is 3.
Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], k = 3
     
Output: 10
Explanation: 10 is the 3rd smallest element in the BST.
Constraints:

1 <= number of nodes, k <= 10^5
1 <= node->data <= 10^5

Solution

Code -
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        stack = []
        current = root
        count = 0
        
        while True:
            while current:
                stack.append(current)
                current = current.left
                
            if not stack:
                break
            
            current = stack.pop()
            count += 1
            if count == k:
                return current.data
            current = current.right
        return -1

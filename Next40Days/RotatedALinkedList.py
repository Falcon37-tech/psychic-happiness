Today's Problem is -

Given the head of a singly linked list, your task is to left rotate the linked list k times.

Examples:

Input: head = 10 -> 20 -> 30 -> 40 -> 50, k = 4
Output: 50 -> 10 -> 20 -> 30 -> 40
Explanation:
Rotate 1: 20 -> 30 -> 40 -> 50 -> 10
Rotate 2: 30 -> 40 -> 50 -> 10 -> 20
Rotate 3: 40 -> 50 -> 10 -> 20 -> 30
Rotate 4: 50 -> 10 -> 20 -> 30 -> 40

Input: head = 10 -> 20 -> 30 -> 40 , k = 6
Output: 30 -> 40 -> 10 -> 20 
 
Constraints:

1 <= number of nodes <= 105
0 <= k <= 109
0 <= data of node <= 109

Solution
Code -

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        if not head or not head.next or k == 0:
            return head
            
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        k %= length
        if k == 0:
            return head
        
        new_tail = head
        for _ in range(k - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        
        new_tail.next = None
        tail.next = head
        
        return new_head
        

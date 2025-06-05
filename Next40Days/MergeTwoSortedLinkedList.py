Today's Problem is -

Merge two sorted linked lists
Difficulty: MediumAccuracy: 62.91%Submissions: 188K+Points: 4Average Time: 30m
Given the head of two sorted linked lists consisting of nodes respectively. The task is to merge both lists and return the head of the sorted merged list.

Examples:

Input: head1 = 5 -> 10 -> 15 -> 40, head2 = 2 -> 3 -> 20
Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40
Explanation:

Input: head1 = 1 -> 1, head2 = 2 -> 4
Output: 1 -> 1 -> 2 -> 4
Explanation:

Constraints:
1 <= no. of nodes<= 103
0 <= node->data <= 105

Solution
Code-

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self,head1, head2):
        dummy = Node(0)
        tail = dummy
        
        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
                
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
            
        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2
        return dummy.next

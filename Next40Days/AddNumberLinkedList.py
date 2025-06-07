Today's Problem is -

Given the head of two singly linked lists num1 and num2 representing two non-negative integers. The task is to return the head of the linked list representing the sum of these two numbers.

For example, num1 represented by the linked list : 1 -> 9 -> 0, similarly num2 represented by the linked list: 2 -> 5. Sum of these two numbers is represented by 2 -> 1 -> 5.

Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

Examples:

Input: num1 = 4 - > 5, num2 = 3 -> 4 -> 5
Output:  3 -> 9 -> 0
 
Explanation: Given numbers are 45 and 345. There sum is 390.
Input: num1 = 0 -> 0 -> 6 -> 3, num2 = 0 -> 7 
Output: 7 -> 0 

Explanation: Given numbers are 63 and 7. There sum is 70.
Constraints:
1 <= size of both linked lists <= 106
0 <= elements of both linked lists <= 9

Expected Complexities
Time Complexity: O(n + m)
Auxiliary Space: O(max(n, m))

Solution
Code -

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def addTwoLists(self, num1: 'Node' , num2: 'Node') -> 'Node' :
        stack1, stack2 = [], []
        
        while num1:
            stack1.append(num1.data)
            num1 = num1.next
            
        while num2:
            stack2.append(num2.data)
            num2 = num2.next
            
        carry = 0
        head = None
        
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            
            total = val1 +val2 + carry
            carry = total // 10
            digit = total % 10
            new_node = Node(digit)
            new_node.next = head
            head = new_node
            
        while head and head.data == 0 and head.next:
            head = head.next
            
        return head

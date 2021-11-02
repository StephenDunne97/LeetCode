"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
LinkedList1: 5 -> 2 -> 1 (125)
LinkedList2: 5 -> 1 -> 1 (115)
Result: 0 -> 4 -> 2 (240)

Logic: 
Go through LinkedList node's until the end, extract data to the beginning of a string giving you a the reversed number
Return reversed number as an int
Repeat for LinkedList2
Add the values together
Reverse result and serparate to individual values in a list
Create a new LinkedList with result

Methods:
-toint() - Converts the values of a LinkedList to a reversed integer
-tolinkedlist(int) - Reverses an integer, splits it into a list, creats Linked List using the list
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = int(linkedListToInt(l1)) + int(linkedListToInt(l2)) # Get sum of Linked-Lists
        ll = stringToLinkedList(str(result)) # Convert sum to Linked-List
        return(ll)        

# The input will be a reversed number e.g: 1 -> 2 -> 3 which in int form should be 321 
def linkedListToInt(LinkedList):
        valid = True # Used to terminate loop
        number = ""
        current = LinkedList # Setting current node to head
        while valid is True:
            if current.next is None: # If at end of Linked-List, take value and exit While loop
                number = str(current.val) + number # Append the current nodes data to beginning of number
                valid = False
            else:
                number = str(current.val) + number # Append the current nodes data to beginning of number
                current = current.next # Move to next node in Linked-List
        return number 

def stringToLinkedList(string):
    string = string[::-1] # Reverse string
    head = None
    for x in string: 
        if head is None:
            head = ListNode(x)
            current = head
        else:
            current.next = ListNode(x)
            current = current.next
    return head
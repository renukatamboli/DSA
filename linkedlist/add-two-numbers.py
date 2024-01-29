# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        newHead = ListNode()
        current = newHead
        carry = 0
        while p1 is not None and p2 is not None:
            val = p1.val+p2.val+carry
            newNode = None
            newVal = val%10
            carry = val//10
            newNode = ListNode(newVal)
            current.next = newNode
            p1 = p1.next
            p2 = p2.next
            current = current.next
            
        while p1 is not None:
            val = p1.val + carry
            newVal = val%10
            carry = val//10
            newNode = ListNode(newVal)
            current.next = newNode
            p1 = p1.next
            current = current.next
            
        while p2 is not None:
            val = p2.val + carry
            newVal = val%10
            carry = val//10
            newNode = ListNode(newVal)
            current.next = newNode
            p2 = p2.next
            current = current.next
        
        if carry != 0:
            newNode= ListNode(carry)
            current.next = newNode
        
        return newHead.next        

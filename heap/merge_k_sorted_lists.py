# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total_list = []
        heap = []
        head = None
        for index,lst in enumerate(lists):
            i = 0
            while lst:
                heappush(heap, (lst.val, index,i, lst))
                lst = lst.next
                i+=1
        prev = None
        while heap:
            val, index,t, node = heappop(heap)
            if not head:
                head = node
            if prev:
                prev.next = node
            prev = node
        return head

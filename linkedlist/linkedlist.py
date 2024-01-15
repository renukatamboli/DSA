class Node:
    
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        self.head = None
        
        

    def get(self, index):
        cur = self.getNode(index)
        if cur!=None:
            return cur.val
        else:
            return -1
        """
        :type index: int
        :rtype: int
        """
    def getNode(self, index):
        cur = self.head
        while index != 0 and cur is not None:
            cur = cur.next
            index-=1
        return cur

    def addAtHead(self, val):
        node = Node(val) 
        node.next = self.head
        self.head = node
        
        
        """
        :type val: int
        :rtype: None
        """
        
    def getTail(self):
        cur = self.head
        while cur is not None and cur.next is not None:
            cur = cur.next
        return cur
        """
        :type index: int
        :type val: int
        :rtype: None
        """
    def addAtTail(self, val):
        if self.head is None:
            self.addAtHead(val)
            return
        prev = self.getTail()
        node = Node(val)
        prev.next = node
        
        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
        prev = self.getNode(index-1)
        if prev is not None:
            cur = Node(val)
            cur.next = prev.next
            prev.next = cur
            
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def deleteAtIndex(self, index):
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
        else:
            prev = self.getNode(index - 1)
            if prev is not None and prev.next is not None:
                prev.next = prev.next.next
            
        """
        :type index: int
        :rtype: None
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class Node:
    
    def __init__(self,val=0):
        self.val = val
        self.next = None
        self.prev = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:            
        node = self.getNode(index)
        if node is not None:
            return node.val
        else:
            return -1
        
    
    def getNode(self,index: int) -> int:
        node = self.head
        while index > 0 and node is not None:
            node = node.next
            index -= 1
        return node
        

    def addAtHead(self, val: int) -> None:
        newHead = Node(val)
        if self.head is not None:
            self.head.prev = newHead
        newHead.next = self.head
        self.head = newHead
        

    def getTail(self) -> Node:
        node = self.head
        while node is not None and node.next is not None:
            node = node.next
        return node
        
    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.addAtHead(val)
            return
        node = self.getTail()
        newTail = Node(val)
        newTail.prev = node
        node.next = newTail
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return 
        prevNode = self.getNode(index - 1)
        if prevNode is not None:
            node = self.getNode(index)
            newNode = Node(val)
            newNode.prev = prevNode
            newNode.next = node
            prevNode.next = newNode
            if node is not None:
                node.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        node = self.getNode(index)
        if node is None:
            return
        prevNode = node.prev
        nextNode = node.next
        if prevNode is None:
            self.head = nextNode
        else:
            prevNode.next = nextNode
        
        if nextNode is not None:
            nextNode.prev = prevNode
            
            
                
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

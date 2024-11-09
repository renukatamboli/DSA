class Node:

    def __init__(self,val,key,prev=None,next=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash_set = {}
    
    def insert(self,node):
        self.hash_set[node.key] = node
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node
    
    def remove(self, node):
        print("node",node,"key", node.key)
        del self.hash_set[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.hash_set:
            node = self.hash_set[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_set:
            node = self.hash_set[key]
            self.remove(node)
        
        if len(self.hash_set.keys()) == self.capacity:
            self.remove(self.tail.prev)
        self.insert(Node(value,key))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

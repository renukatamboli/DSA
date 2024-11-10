class Node:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.cnt = 1
        self.prev = None
        self.next = None

class List:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addFront(self,node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
        self.size += 1
    
    def removeNode(self, delNode):
        delprev = delNode.prev
        delnext = delNode.next
        delprev.next = delnext
        delnext.prev = delprev
        res = self.head
        self.size -= 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_set = {}
        self.freq_map = {}
        self.cursize = 0
        self.minfreq = 0
    
    def updatefreqListMap(self, node):
        del self.hash_set[node.key]
        self.freq_map[node.cnt].removeNode(node)
        if node.cnt == self.minfreq and self.freq_map[node.cnt].size == 0:
            self.minfreq += 1
        nextHighFreqLst = List()
        node.cnt += 1
        if node.cnt in self.freq_map:
            nextHighFreqLst = self.freq_map[node.cnt]
        nextHighFreqLst.addFront(node)
        self.freq_map[node.cnt] = nextHighFreqLst
        self.hash_set[node.key] = node

    def get(self, key: int) -> int:
        if key in self.hash_set:
            node = self.hash_set[key]
            self.updatefreqListMap(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.hash_set:
            node = self.hash_set[key]
            node.val = value
            self.updatefreqListMap(node)
        else:
            if self.cursize == self.capacity:
                lst = self.freq_map[self.minfreq]
                del self.hash_set[lst.tail.prev.key]
                self.freq_map[self.minfreq].removeNode(lst.tail.prev)
                self.cursize-=1
            self.cursize+=1
            self.minfreq = 1
            lstfreq = List()
            if self.minfreq in self.freq_map:
                lstfreq = self.freq_map[self.minfreq]
            node = Node(key,value)
            lstfreq.addFront(node)
            self.hash_set[key] = node
            self.freq_map[self.minfreq] = lstfreq


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

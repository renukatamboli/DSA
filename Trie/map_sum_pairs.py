class Node:
    
    def __init__(self):
        self.links = [None for _ in range(26)]
        self.flag = 0
        
    def containsKey(self,ch):
        return self.links[ord(ch) - ord('a')] is not None
    
    def get(self,ch):
        return self.links[ord(ch) - ord('a')]
    
    def put(self,ch, node):
        self.links[ord(ch) - ord('a')] = node
        
    def setEnd(self, val):
        self.flag = val
        
    def isEnd(self):
        return self.flag > 0
        
class MapSum:

    def __init__(self):
        self.root = Node()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map.get(key, 0)
        self.map[key] =  val
        
        node = self.root
        for ch in key:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
            node.flag += diff
                
    
    def sum(self, prefix: str) -> int:
        node = self.root
        for i in range(0,len(prefix)):
            if not node.containsKey(prefix[i]):
                return 0
            node = node.get(prefix[i])
        return node.flag
            
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

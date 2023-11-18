class Node:
    def __init__(self):
        self.links = [None for _ in range(26)]
        self.flag = False
        
    def containsKey(self,ch):
        return self.links[ord(ch)-ord('a')] is not None
    
    def get(self,ch):
        return self.links[ord(ch)-ord('a')]
    
    def put(self,ch,node):
        self.links[ord(ch)-ord('a')] = node
    
    def setEnd(self):
        self.flag = True
    
    def isEnd(self):
        return self.flag
      
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self,word):
        node = self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i],Node())
            node = node.get(word[i])
        node.setEnd()
    
    def search(self,word):
        node = self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                return False
            node = node.get(word[i])
        return node.isEnd()
    
    def startsWith(self,word):
        node = self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                return False
            node = node.get(word[i])
        return True

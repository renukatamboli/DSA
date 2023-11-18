class Node:
    def __init__(self):
        self.links = [None for _ in range(26)]
        self.cntEndWith = 0
        self.cntPrefix = 0
        
    def containsKey(self,ch):
        return self.links[ord(ch)-ord('a')] is not None
    
    def get(self,ch):
        return self.links[ord(ch)-ord('a')]
    
    def put(self,ch,node):
        self.links[ord(ch)-ord('a')] = node
    
    def increaseEnd(self):
        self.cntEndWith+=1

    def deleteEnd(self):
        self.cntEndWith-=1
        
    def increasePrefix(self):
        self.cntPrefix+=1
        
    def deletePrefix(self):
        self.cntPrefix-=1
      
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self,word):
        node = self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i],Node())
            node = node.get(word[i])
            node.increasePrefix()
        node.increaseEnd()
    
    def countWordsEqualTo(self,word):
        node = self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                return 0
            node = node.get(word[i])
        return node.cntEndWith
    
    def countWordStartsWith(self,word):
        node = self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                return 0
            node = node.get(word[i])
        return node.cntPrefix
        
    def erase(self,word):
        node = self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                return
            node = node.get(word[i])
            node.deletePrefix()
        return node.deleteEnd()

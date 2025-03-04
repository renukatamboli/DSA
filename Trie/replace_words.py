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
        
    def setEnd(self):
        self.flag = True
        
    def isEnd(self):
        return self.flag
    
class Solution:
    
    def __init__(self):
        self.root = Node()
        
    def insert(self,word):
        node = self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i],Node())
            node = node.get(word[i])
        node.setEnd()
    
    def startsWith(self,word):
        node = self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                return False
            node = node.get(word[i])
            if node.isEnd():
                return word[0:i+1]
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        node = self.root
        for item in dictionary:
            self.insert(item)
        words = sentence.split(' ')
        for i in range(len(words)):
            start = self.startsWith(words[i])
            if start:
                words[i] = start
        return ' '.join(words)
        

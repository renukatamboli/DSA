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
    
    def checkIfPrefixExists(self,word):
        node = self.root
        for i in range(0,len(word)):
            if node.containsKey(word[i]):
                node = node.get(word[i])
                if not node.isEnd():
                    return False
            else:
                return False
        return True
      
def lonestPrefixContains(words):
    trie = Trie()
    longest = ''
    for word in words:
        trie.insert(word)
    for word in words:
        if trie.checkIfPrefixExists(word):
            if len(word)>len(longest):
                longest = word
            elif len(word)>len(longest) and word<longest:
                longest = word
    return longest

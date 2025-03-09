class Node:
    
    def __init__(self):
        self.links = [None for _ in range(26)]
        self.flag = False
        
    def containsKey(self,ch):
        if ch == '.':
            return False
        return self.links[ord(ch) - ord('a')] is not None
    
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
    
    def put(self,ch, node):
        self.links[ord(ch) - ord('a')] = node
    
    def setEnd(self):
        self.flag = True
        
    def isEnd(self):
        return self.flag
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
        node.setEnd()

    def startsWith(self,word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return True
    
    def searchWord(self,word, node):
        for i,ch in enumerate(word):
            if not node.containsKey(ch):
                if ch == ".":
                    for x in node.links:
                        if x and self.searchWord(word[i+1:],x):
                            return True
                return False
            node = node.get(ch)
        return node.isEnd()
    
    def search(self, word: str) -> bool:
        node = self.root
        return self.searchWord(word,node)
     


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

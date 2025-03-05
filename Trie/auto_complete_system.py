class Node:
    
    def __init__(self):
        self.links = [None for _ in range(27)]
        self.map = {}
        self.flag = False
        
    def containsKey(self,ch):
        #print("\n ch", ch)
        if ch == ' ':
            return self.links[0] is not None 
        return self.links[ord(ch) - ord('a') + 1] is not None
    
    def get(self,ch):
        if ch == " ":
            return self.links[0]
        return self.links[ord(ch) - ord('a') + 1]
    
    def put(self,ch, node):
        if ch == " ":
            self.links[0] = node
        else:
            self.links[ord(ch) - ord('a') + 1] = node
        
    def setEnd(self):
        self.flag = True
        
    def isEnd(self):
        return self.flag
    
    
class AutocompleteSystem:
    
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Node()
        self.starts = ''
        for i in range(len(sentences)):
            self.insert(sentences[i], times[i])
        
    def insert(self,sentence, time):
        node = self.root
        for i in range(0,len(sentence)):
            if not node.containsKey(sentence[i]):
                node.put(sentence[i],Node())
            node = node.get(sentence[i])
            if not node.map.get(sentence):
                node.map[sentence] = 0
            node.map[sentence] += time
            #print("node", node.map,"sentence",sentence)
            node.map = dict(sorted(node.map.items(), key=lambda x: (-x[1], x[0])))
        node.setEnd()    
        
    def startsWith(self,word):
        node = self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                return []            
            node = node.get(word[i])
        return list(node.map.keys())[:3]
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.insert(self.starts,1)
            self.starts = ''
            return []
        self.starts += c
        return self.startsWith(self.starts)
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

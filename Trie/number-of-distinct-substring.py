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
def getAllSubString(word):
    root = Node()
    count = 0
    for i in range(len(word)-1):
        node = root
        for j in range(i,len(word)):
            if not node.containsKey(word[j]):
                count+=1
                node.put(word[j],Node())
            node = node.get(word[j])
    return count+1 #+1 including empty one

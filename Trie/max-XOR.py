#https://www.codingninjas.com/studio/problems/maximum-xor_973113?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTabValue=SUBMISSION
class Node:

    def __init__(self):
        self.links = [None for _ in range(2)]
    
    def get(self,bit):
        return self.links[bit]
    
    def put(self,bit,node):
        self.links[bit] = node
    
    def containsKey(self,bit):
        return self.links[bit] is not None
    
class Trie:

    def __init__(self):
        self.root = Node()
    
    def insert(self,num):
        node = self.root
        for i in range(31,-1,-1):
            bit = (num >> i) & 1
            if not node.containsKey(bit):
                node.put(bit,Node())
            node = node.get(bit)
          
    def getMax(self,num):
        node = self.root
        maxNum = 0
        for i in range(31,-1,-1):
            bit = (num >> i) & 1
            if node.containsKey(1-bit):
                maxNum = maxNum | 1<<i
                node = node.get(1-bit)
            else:
                node = node.get(bit)
        return maxNum

def maxXOR(n, m, arr1, arr2):
    trie = Trie()
    for i in range(0,n):
        trie.insert(arr1[i])

    maxXOR = 0
    for j in range(0,m):
        maxXOR = max(maxXOR,trie.getMax(arr2[j]))
    return maxXOR


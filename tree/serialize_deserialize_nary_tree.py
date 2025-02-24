"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:        
    
    def solve(self,root):
        if not root:
            return ''
        ans = '['
        ans += str(root.val)
        if root.children:
            for child in root.children:
                ans += self.solve(child)
        ans += ']'
        return ans
        
    def serialize(self, root: 'Node') -> str: 
        if not root:
            return ''
        ans = ''
        ans += self.solve(root)
        print("ans", ans)
        return ans
            
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        
	
    def deserialize(self, data: str) -> 'Node':
        if data == '':
            return
        stack = []
        obj = []
        i = 0
        l = len(data)
        head = None
        while i < l:
            if data[i] == "[" or data[i] == "]":
                obj.append(data[i])
                i+=1
            else:
                num = ''
                while data[i] != "[" and data[i] != "]":
                    num += data[i]
                    i+=1
                node = Node(int(num),[])
                obj.append(node)
        for item in obj:
            if item != "]":
                stack.append(item)
            else:
                node = stack.pop()
                stack.pop()
                if stack:
                    parent = stack[-1]
                    parent.children.append(node)
                else:
                    head = node
        return head
                
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

import math
class Solution:
    def numSquares(self, n: int) -> int:
        queue = []
        queue.append(n)
        
        steps = 0
        visited = set()
        
        while len(queue)>0:
            
            size = len(queue)
            
            while size>0:
                node = queue.pop(0)
                
                if node == 0:
                    return steps
                
                n1 = math.floor(math.sqrt(node))
                for i in range(n1,0,-1):
                    if node-i*i not in visited:
                        visited.add(node-i*i)
                        queue.append(node - i*i)
                    
                size-=1
            steps+=1
                    
        
        return steps
        
        

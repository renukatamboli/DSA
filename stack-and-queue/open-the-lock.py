class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = []
        steps = 0
        
        queue.append("0000")
        visited = set()
        
        while len(queue) > 0:
            #print("queue",queue)
            size = len(queue)
            
            while size>0:
                
                node = queue.pop(0)
                
                size = size-1
            
                if node in deadends:
                    continue
            
                if node == target:
                    return steps
                
                temp = list(node)
            
                for i in range(4):
                    num = int(temp[i])
                    for diff in [-1, 1]:
                        newNum = (num + diff) % 10  
                        temp_copy = temp[:]     
                        temp_copy[i] = str(newNum)

                        tempstr = "".join(temp_copy)

                        if tempstr in deadends or tempstr in visited:
                            continue

                        if tempstr == target:
                            return steps + 1

                        visited.add(tempstr)
                        queue.append(tempstr)


            steps = steps+1
        return -1
        
        

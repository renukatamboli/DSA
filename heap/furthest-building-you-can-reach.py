from queue import PriorityQueue

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        if not heights:
            return 0
        
        q = PriorityQueue()
        i = 0
        
        while i < len(heights) - 1 and ladders > 0:
            if heights[i] < heights[i+1]:
                q.put(heights[i+1] - heights[i])
                ladders -= 1
            i += 1
        while i < len(heights) - 1:
            if heights[i+1] > heights[i]:
                diff = heights[i+1] - heights[i]
                if not q.empty():
                    bricks_needed = q.get()
                    if diff >= bricks_needed:
                        if bricks < bricks_needed:
                            return i
                        bricks -= bricks_needed
                        q.put(diff)
                    else:
                        q.put(bricks_needed)
                        if bricks < diff:
                            return i
                        else:
                            bricks -= diff
                elif bricks < diff:
                    return i
                else:
                    bricks -= diff
            i += 1
        return i
            
                
                
                    
                
                
                    
                    
                
                
                
                
        
        

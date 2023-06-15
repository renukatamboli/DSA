#User function Template for python3

from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        mod = 100000
        queue = []
        dist = [1e9 for i in range(0, 100000)]
        dist[start] = 0
        queue.append((start,0))
        while(len(queue) > 0):
            it = queue.pop(0)
            node = it[0]
            steps = it[1]
            for v in arr:
                num = (node * v) % mod
                if steps+1 < dist[num]:
                    dist[num] = steps + 1
                    if num == end:
                        return steps+1
                    queue.append((num,steps+1))
        return -1
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends

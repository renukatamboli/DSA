#User function Template for python3
from queue import PriorityQueue
class Solution:
        
    def MinimumEffort(self, a):
        n = len(a)
        m = len(a[0])
        dist = [[1e9 for i in range(0,m)] for j in range(0, n)]
        queue = PriorityQueue()
        dist[0][0] = 0
        queue.put((0,0,0))
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]
        while(queue.qsize()>0):
            node = queue.get()
            dis = node[0]
            row = node[1]
            col = node[2]
            
            #print("row", row, "col", col, "node", node,"n" ,n ,"m", m)
            if row == n-1 and col == m-1:
                return dis
            for i in range(0,4):
                newr = row + delta_row[i]
                newc = col + delta_col[i]
                if(newr >= 0 and newr < n and newc >=0 and newc < m):
                    newEffort = max(dis, abs(a[newr][newc] - a[row][col]))
                    if dist[newr][newc] > newEffort:
                       dist[newr][newc] = newEffort
                       queue.put((dist[newr][newc], newr, newc))
        return 0    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n,m=map(int,input().split())
        a=[]
        for i in range(n):
            li=list(map(int,input().split()))
            a.append(li)
        ob = Solution()
        ans = ob.MinimumEffort(a)
        print(ans)
        tc -= 1
# } Driver Code Ends

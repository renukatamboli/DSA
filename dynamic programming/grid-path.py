#https://practice.geeksforgeeks.org/problems/number-of-paths0926/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
#User function Template for python3

class Solution:
    def find(self,n,m):
        if n==0 and m == 0:
            return 1
        if n < 0 or m < 0:
            return 0
        left = self.find(n,m-1)
        up = self.find(n-1,m)
        return left+up
        
    def numberOfPaths (self, n, m):
        return self.find(n-1,m-1)
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)




# } Driver Code Ends

#https://practice.geeksforgeeks.org/problems/maximum-number-of-coins--170647/1
#User function Template for python3

class Solution():
    def find(self,i,j,a,dp):
        if i>j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        maxi = 0
        for k in range(i,j+1):
            value = a[i-1]*a[k]*a[j+1] + self.find(i,k-1,a,dp) + self.find(k+1,j,a,dp)
            maxi = max(maxi,value)
        
        dp[i][j] = maxi
        return dp[i][j]
        
    def maxCoins(self, N, a):
        a.insert(0,1)
        a.append(1)
        dp = [[-1 for _ in range(0,N+1)] for _ in range(0,N+1)]
        return self.find(1,N,a,dp)
        #your code goes here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(Solution().maxCoins(n, a))
# } Driver Code Ends

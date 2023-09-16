class Solution:
    def find(self,i,j,s,t,dp):
        if i < 0:
            return j+1
        if j < 0:
            return i+1
        if dp[i][j] != -1:
            return dp[i][j]
        if s[i] == t[j]:
            dp[i][j] = self.find(i-1,j-1,s,t,dp)
        else:
            dp[i][j] = min((1+self.find(i,j-1,s,t,dp)),(1+self.find(i-1,j,s,t,dp)),(1+self.find(i-1,j-1,s,t,dp)))
	    return dp[i][j]
	    
	def editDistance(self, s, t):
	    dp = [[-1 for _ in range(len(t))] for _ in range(len(s))]
	    return self.find(len(s)-1,len(t)-1,s,t,dp)
		# Code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends

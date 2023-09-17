# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    def find(self, i,j,pattern, string,dp):
        if i < 0 and j < 0:
            return True
        if i < 0 and j >= 0:
            return False
        if i >= 0 and j < 0:
            for t in range(i+1):
                if pattern[t] != "*":
                    return False
            return True
        if dp[i][j] != -1:
            return dp[i][j]
        if pattern[i] == string[j] or pattern[i] == "?":
            dp[i][j] = self.find(i-1,j-1,pattern,string,dp)
            return dp[i][j]
        if pattern[i] == "*":
            dp[i][j] = self.find(i,j-1,pattern,string,dp) or self.find(i-1,j,pattern,string,dp)
            return dp[i][j]
        dp[i][j] = False
        return dp[i][j]
        
    def wildCard(self,pattern, string):
        dp = [[-1 for i in range(0,len(string))] for j in range(0,len(pattern))]
        return self.find(len(pattern)-1,len(string)-1,pattern,string,dp)
        # Code here



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends

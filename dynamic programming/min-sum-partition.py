#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
	    target = sum(arr)
	    dp = [False for _ in range(target+1)]
        
        dp[0] = True
            
        if arr[0] <= target:
            dp[arr[0]] = True
        
        for i in range(1, N):
            temp = [False for _ in range(target+1)]
            for j in range(1, target+1):
                take = False
                if j >= arr[i]:
                    take = dp[j - arr[i]]
                notTake = dp[j]
                temp[j] = take or notTake
            dp = temp[:]
        mini = 1e9
        for i in range(0,target+1):
            if dp[i]:
                s1 = i
                s2 = target-i
                mini = min(mini,abs(s1-s2))
        return mini
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends

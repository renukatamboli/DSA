#User function Template for python3

class Solution:

	def LongestBitonicSequence(self, nums):
	    dp1 = [1 for _ in range(0,len(nums))]
	    dp2 = [1 for _ in range(0,len(nums))]
	    maxi = 1
	    for i in range(0,len(nums)):
	        for j in range(0,i):
	            if nums[j] < nums[i] and dp1[j]+1 > dp1[i]:
	                dp1[i] = dp1[j]+1
	    for ind in range(len(nums)-1,-1,-1):
	        for prev in range(len(nums)-1,ind,-1):
	            if nums[prev] < nums[ind] and dp2[prev]+1 > dp2[ind]:
	                dp2[ind] = dp2[prev]+1
	    for i in range(0,len(nums)):
	        maxi = max(maxi,dp1[i]+dp2[i]-1)
	    return maxi
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.LongestBitonicSequence(nums)
		print(ans)
# } Driver Code Ends

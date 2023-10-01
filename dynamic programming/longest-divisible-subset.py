#User function Template for python3

class Solution:
    def LargestSubset(self, n, arr):
        arr.sort()
        dp = [0 for _ in range(0,n+1)]
        h = [i for i in range(0,n)]
        maxi = 0
        lastIndex = 0
        for ind in range(0,n):
            for prev in range(0,ind):
                if arr[ind] % arr[prev] == 0 and 1 + dp[prev] > dp[ind]:
                    dp[ind] = 1 + dp[prev]
                    h[ind] = prev
                    
                if dp[ind] > maxi:
                    lastIndex = ind
                    maxi = dp[ind]
        temp = []
        temp.append(arr[lastIndex])
        while(h[lastIndex]!=lastIndex):
            lastIndex = h[lastIndex]
            temp.append(arr[lastIndex])
        temp.reverse()
        return temp
            
        #Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.LargestSubset(n,arr)
        isValidSeq, sz = 1, len(res)
        for i in range(sz):
            for j in range(i + 1, sz):
                if (res[i] % res[j] == 0) or (res[j] % res[i] == 0):
                    continue
                else:
                    isValidSeq = 0
                    break
        print(isValidSeq, sz)
# } Driver Code Ends

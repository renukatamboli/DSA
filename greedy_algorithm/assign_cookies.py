#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def maxChildren(self, greed, cookie):
        greed.sort()
        cookie.sort()
        i = 0
        j = 0
        ans = 0
        while i < len(cookie) and j < len(greed):
            if cookie[i] >= greed[j]:
                j+=1
                ans += 1
                i+=1
            else:
                i+=1
        return ans
        #Your code goes here.


#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())
    for _ in range(t):
        greed = list(map(int, input().strip().split()))
        cookie = list(map(int, input().strip().split()))

        obj = Solution()
        print(obj.maxChildren(greed, cookie))
        print("~")

if __name__ == "__main__":
    main()
# } Driver Code Ends

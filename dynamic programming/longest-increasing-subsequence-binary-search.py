#User function Template for python3

class Solution:
    def getInd(self,low,high,temp,num):
        if low >= high:
            return low
        mid = int((low+high)/2)
        if temp[mid] >= num:
            return self.getInd(low,mid,temp,num)
        else:
            return self.getInd(mid+1,high,temp,num)
        
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        temp =  []
        temp.append(a[0])
        l = 1
        for i in range(1,n):
            if a[i] > temp[len(temp)-1]:
                temp.append(a[i])
                l+=1
            else:
                ind = self.getInd(0,len(temp),temp,a[i])
                temp[ind] = a[i]
        return l
        # code here
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends

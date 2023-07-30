class Solution:
    def __init__(self):
        self.cnt = 0
        
    def merge(self,low,mid,high,nums):
        left = low
        right = mid+1
        temp = []
        while(left<=mid and right<=high):
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
                self.cnt += (mid-left+1)
        while(left<=mid):
            temp.append(nums[left])
            left+=1
        while(right<=high):
            temp.append(nums[right])
            right+=1
        for i in range(low,high+1):
            nums[i] = temp[i-low]

    def mergeSort(self,low,high,nums):
        if(low < high):
            mid = (low + high) // 2
            self.mergeSort(low,mid,nums)
            self.mergeSort(mid+1,high,nums)
            self.merge(low,mid,high,nums)
        
    def inversionCount(self, arr, n):
        self.mergeSort(0,len(arr)-1,arr)
        return self.cnt
        # Your Code Here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends

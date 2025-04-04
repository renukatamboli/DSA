from heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        l = len(nums)
        i = 0
        while i < l:
            while heap and i - heap[0][1] >= k:
                heappop(heap)
            heappush(heap,(-nums[i],i))
            if i >= k-1:
                value, index = heap[0]
                ans.append(-value)
            i+=1
            
        # print("heap here", heap)
        # print("ans here")
        # value, index = heap[0]
        # ans.append(-value)
        return ans
        
        

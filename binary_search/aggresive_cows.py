class Solution:
    def check(self,arr,k,m):
        last = arr[0]
        cnt = 1
        for pos in arr:
            if pos-last >= k:
                cnt+=1
                last = pos
            if cnt >= m:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low = 1
        high = position[-1]-position[0]
        while low <= high:
            mid = (low+high) // 2
            if self.check(position,mid,m):
                low = mid+1
            else:
                high = mid-1
        return high

        

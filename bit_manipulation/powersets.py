class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = 2 ** len(nums)
        n = len(nums)
        ans = []
        for num in range(subset):
            sub = []
            for i in range(0,n):
                if(num & (1<<i)):
                    sub.append(nums[i])
            ans.append(sub[:])
        return ans 

        

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        if not nums:
            return ans
        n = len(nums)
        nums.sort()
        for i in range(0,n):
            for j in range(i+1,n):
                target2 = target - (nums[i] + nums[j])
                front = j+1
                back = n-1
                while front < back:
                    two_sum = nums[front] + nums[back]
                    if two_sum < target2:
                        front+=1
                    elif two_sum > target2:
                        back-=1
                    else:
                        quad = (nums[i],nums[j], nums[front], nums[back])
                        ans.add(quad)
                        front+=1
                        back-=1
                        while front < back and nums[front] == quad[2]:
                            front+=1
                        while front < back and nums[back] == quad[3]:
                            back-=1
        return list(ans)

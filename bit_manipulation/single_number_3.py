class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        b1 = 0
        b2 = 0
        for num in nums:
            xor = xor ^ num
        rightmost = ((xor) ^ (xor-1)) & xor
        for num in nums:
            if rightmost & num:
                b1 = b1 ^ num
            else:
                b2 = b2 ^ num
        return [b1,b2] 
        

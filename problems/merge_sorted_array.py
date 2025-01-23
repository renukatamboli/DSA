class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = m-1
        k = 0
        while i < m+n and k < n:
            if nums1[i] >= nums2[k]:
                temp = j
                while temp >= i and temp < m+n:
                    nums1[temp+1] = nums1[temp]
                    temp-=1
                nums1[i] = nums2[k]
                j+=1
                k+=1
            else:
                if i > j:
                    j+=1
                    nums1[j] = nums2[k]
                    k+=1
            i+=1

        

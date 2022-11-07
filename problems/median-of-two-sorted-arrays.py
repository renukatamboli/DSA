import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        merged_array = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_array.append(nums1[i])
                i+=1
            else:
                merged_array.append(nums2[j])
                j+=1
        while i < len(nums1):
            merged_array.append(nums1[i])
            i+=1
        while j < len(nums2):
            merged_array.append(nums2[j])
            j+=1
        l = len(merged_array)
        if l%2 == 0:
            index1 = math.floor(l/2)
            index2 = index1-1
            return ( merged_array[index1] + merged_array[index2] ) /2
        else:
            return merged_array[math.floor(l/2)]
        
       
            
            
#https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/

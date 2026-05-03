# https://leetcode.com/problems/find-in-mountain-array/
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:

    def find(self, arr, l, h, target):
        while l < h:
            mid = (l + h) // 2
            if arr.get(mid) == target:
                return mid
            elif arr.get(mid) < target:
                l = mid + 1
            else:
                h = mid
        return -1

    def findreverse(self, arr, l, h, target):
        while l < h:
            mid = (l + h) // 2
            if arr.get(mid) == target:
                return mid
            elif arr.get(mid) > target:
                l = mid + 1
            else:
                h = mid
        if arr.get(l) == target:
            return l
        return -1

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 0
        h = mountainArr.length() - 1
        while l < h:
            mid = (l+h) // 2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid + 1
            else:
                h = mid
        peak = l
        print("peak", peak)
        l = 0
        h = mountainArr.length() - 1
        index = self.find(mountainArr, l, peak, target)
        print("index", index)
        if index != -1:
            return index
        print("here")
        return self.findreverse(mountainArr, peak, h, target)




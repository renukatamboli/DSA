class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = 0
        r = 0
        while l < len(arr)-1:
            if arr[l] == 0:
                r = len(arr)-1
                while r > l+1:
                    arr[r] = arr[r-1]
                    r-=1
                #print("arr", arr,"l", l)
                arr[l+1] = 0
                l+=1
            l+=1
        return arr
                
                

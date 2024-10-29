class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        n = len(arr)
        arr.sort()
        dep.sort()
        i  = 1
        j = 0
        platforms = 1
        result = 1
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms += 1
                i+=1
            else:
                platforms -= 1
                j+=1
                
            if platforms > result:
                result = platforms
                
        return result

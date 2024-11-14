class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hash_set = {}
        l = 0
        r = 0
        maxlen = 0
        n = len(fruits)
        while r < n:
            if fruits[r] not in hash_set:
                hash_set[fruits[r]] = 1
            else:
                hash_set[fruits[r]] += 1

            while len(hash_set)> 2:
                hash_set[fruits[l]]-=1
                if hash_set[fruits[l]] == 0:
                    del hash_set[fruits[l]]
                l+=1
            maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen    

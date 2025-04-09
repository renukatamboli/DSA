from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        freq = defaultdict(int)
        heap = []
        for char in s:
            freq[char] += 1
        for char,value in freq.items():
            heappush(heap, (-value,char))
        while heap:
            value, char = heappop(heap)
            ans += char*(-value)
        return ans

        

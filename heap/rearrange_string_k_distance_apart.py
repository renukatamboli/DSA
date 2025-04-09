from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        free = []
        busy = []
        ans = []
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        for char, value in freq.items():
            heappush(free, (-freq[char], char))
        while len(ans) != len(s):
            index = len(ans)
            if busy and index-busy[0][0] >= k:
                busy_index, busy_value = heappop(busy)
                heappush(free,(-freq[busy_value], busy_value))
            if not free:
                return ''
            count, value = heappop(free)
            count = -count-1
            freq[value] = count
            ans.append(value) 
            if count > 0:
                heappush(busy,(index, value))
        return ''.join(ans)
            


            
            

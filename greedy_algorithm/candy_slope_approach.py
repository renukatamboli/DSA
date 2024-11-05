class Solution:
    def candy(self, ratings: List[int]) -> int:
        i = 1
        s = 1
        n = len(ratings)
        while i < n:
            if ratings[i] == ratings[i-1]:
                s = s+1
                i+=1
                continue
            peak = 1
            while i < n and ratings[i] > ratings[i-1]:
                peak+=1
                s += peak
                i+=1
            down = 1
            while i < n and ratings[i] < ratings[i-1]:
                s += down
                down += 1
                i+=1
            if down > peak:
                s = s+ (down-peak)
        return s

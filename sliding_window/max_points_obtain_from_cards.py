class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        n = len(cardPoints)
        total = 0
        for i in range(n):
            total = total + cardPoints[i]
        score = 0
        r = n-k-1
        s = 0
        for i in range(l,r+1):
            s = s+cardPoints[i]
        score = max(score,total-s)
        r += 1
        while r < n:
            s = s-cardPoints[l]
            s = s+cardPoints[r]
            score = max(score,total-s)
            l+=1
            r+=1
        return score
        

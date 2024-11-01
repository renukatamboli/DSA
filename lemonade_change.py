from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cost = 5
        change = defaultdict(int)
        for bill in bills:
            if bill == 5:
                change[5] += 1
            if bill == 10:
                if change[5] > 0:
                    change[5] -= 1
                else:
                    return False
                change[10] += 1
            if bill == 20:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
        return True

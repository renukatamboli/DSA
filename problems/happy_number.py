class Solution(object):
    def isHappy(self, n):
        slow = n
        fast = n
        while(fast!=1 and self.sum(fast)!=1):
            slow = self.sum(slow)
            fast = self.sum(self.sum(fast))
            if(slow == fast):
                return False
        return True
        """
        :type n: int
        :rtype: bool
        """
    def sum(self,n):
        return sum([pow(int(x),2) for x in str(n)])

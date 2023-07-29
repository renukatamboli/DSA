class Solution(object):
    def isPallindrome(self,s):
        for i in range(0,int(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
    def doPartition(self, index, s, ans,ds):
        if index == len(s):
            ans.append(ds[:])
            return
        for i in range(index+1,len(s)+1):
            if(self.isPallindrome(s[index:i])):
                ds.append(s[index:i])
                self.doPartition(i,s,ans,ds)
                ds.pop()

    def partition(self, s):
        ds = []
        ans = []
        self.doPartition(0, s, ans,ds)
        return ans
        """
        :type s: str
        :rtype: List[List[str]]
        """

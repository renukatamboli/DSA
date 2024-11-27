class Solution:
    def solve(self,n,k,ans,temp,i):
        if i == n+1:
            if len(temp) == k:
                ans.append(temp[:])
                temp = []
            return
        if len(temp) == k:
            ans.append(temp[:])
            temp = []
            return
        for j in range(i,n+1):
            temp.append(j)
            self.solve(n,k,ans,temp,j+1)
            temp.remove(j)
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        temp = []
        self.solve(n,k,ans,temp,1)
        return ans
        

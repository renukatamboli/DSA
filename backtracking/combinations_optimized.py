class Solution:
    def solve(self,n,k,ans,temp,i):
        if len(temp) == k:
            ans.append(temp[:])
            return

        need = k - len(temp)
        remain = n - i + 1
        available = remain - need
        for j in range(i,i+available+1):
            temp.append(j)
            self.solve(n,k,ans,temp,j+1)
            temp.pop()
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        temp = []
        self.solve(n,k,ans,temp,1)
        return ans
        

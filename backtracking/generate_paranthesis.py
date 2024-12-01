class Solution:
    def solve(self,queue,ans,temp,ocnt,ccnt,n):
        if ocnt == n and ccnt == n and not queue:
            ans.append(''.join(temp[:]))
            return
        if queue:
            queue.pop()
            temp.append(")")
            ccnt+=1
            self.solve(queue,ans,temp,ocnt,ccnt,n)
            temp.pop()
            ccnt-=1
            queue.append("(")
        if ocnt < n:
            queue.append("(")
            temp.append("(")
            ocnt+=1
            self.solve(queue,ans,temp,ocnt,ccnt,n)
            ocnt-=1
            temp.pop()
            queue.pop()
        
    def generateParenthesis(self, n: int) -> List[str]:
        queue = []
        ans = []
        temp = ["("]
        ocnt = 1
        ccnt = 0
        queue.append("(")
        self.solve(queue,ans,temp,ocnt,ccnt,n)
        return ans
        

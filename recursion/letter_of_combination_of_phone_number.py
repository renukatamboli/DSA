class Solution:
    def solve(self,digits,mapping,ans,temp, index):
        if index == len(digits):
            ans.append(''.join(temp[:]))
            return
        
        for char in mapping[digits[index]]:
            temp.append(char)
            self.solve(digits,mapping,ans,temp,index+1)
            temp.pop()
        
        
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = []
        temp = []
        self.solve(digits,mapping,ans,temp,0)
        return ans

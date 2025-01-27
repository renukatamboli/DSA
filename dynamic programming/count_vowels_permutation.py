class Solution:
    def solve(self, dp, n, i, vowel, mod=10**9+7):
        if i == 0:
            return 1
        if dp[i][vowel] != -1:
            return dp[i][vowel]
        
        if vowel == 0:  
            dp[i][vowel] = self.solve(dp, n, i-1, 1, mod)  # 'e'
        elif vowel == 1:  
            dp[i][vowel] = (self.solve(dp, n, i-1, 0, mod) + self.solve(dp, n, i-1, 2, mod)) % mod  # 'a' + 'i'
        elif vowel == 2:  
            dp[i][vowel] = (self.solve(dp, n, i-1, 0, mod) +
                            self.solve(dp, n, i-1, 1, mod) +
                            self.solve(dp, n, i-1, 3, mod) +
                            self.solve(dp, n, i-1, 4, mod)) % mod  # 'a', 'e', 'o', 'u'
        elif vowel == 3:  # 'o'
            dp[i][vowel] = (self.solve(dp, n, i-1, 2, mod) + self.solve(dp, n, i-1, 4, mod)) % mod  # 'i' + 'u'
        elif vowel == 4:  # 'u'
            dp[i][vowel] = self.solve(dp, n, i-1, 0, mod)  # 'i'
        
        return dp[i][vowel]
    
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9+7
        dp = [[-1 for _ in range(5)] for _ in range(n)]  
        result = 0
        
        for vowel in range(5):
            result = (result + self.solve(dp, n, n-1, vowel, mod)) % mod
        
        return result

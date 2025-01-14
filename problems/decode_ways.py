class Solution:        
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]

        if s[0] == "0":
            return 0
        
        dp[0] = 1
        dp[1] = 1
        
            
        for i in range(2,len(s)+1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            two_digit = s[i-2:i]
            if int(two_digit) >= 10 and int(two_digit) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
            

def lcs(x,y,s1,s2):
    dp = [[-1 for i in range(0,y+1)] for j in range(0,x+1)]
    string = [["" for i in range(0,y+1)] for j in range(0,x+1)]
    for j in range(0,y+1):
        dp[0][j] = 0
    for i in range(0,x+1):
        dp[i][0] = 0
    for i in range(1,x+1):
        for j in range(1,y+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                string[i][j] = s1[i-1] + string[i-1][j-1]
            else:
                if dp[i-1][j]>=dp[i][j-1]:
                    dp[i][j] = dp[i - 1][j]
                    string[i][j] = string[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
                    string[i][j] = string[i][j-1]
    return string[x][y]

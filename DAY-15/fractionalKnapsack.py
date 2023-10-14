def kanpsack(W,wt,val,n):
    dp=[[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if w==0 or i==0 :
                dp[i][w]=0
            elif wt[i-1]<w:
                dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][W]




def cost(m,r,c):
    dp=[0 [for i in range(r)] for j in range(c)]
    print(dp)
    for i in range(c):
        dp[0][i]=m[0][i]
    for i in range(1,r):
        for j in range(c):
            if j==0:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j+1])+m[i][j]
            elif j==c-1:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+m[i][j]
            else:
                dp[i][j]=max(dp[i-1][j],max(dp[i-1][j-1],dp[i-1][j+1]))+m[i][j]
    print(dp)

m=[]
cost(m,r,c)
 
   


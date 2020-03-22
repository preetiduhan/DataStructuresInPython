def longest_palindrome(s):
    n=len(s)
    p=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        p[i][i]=1
    maxlength=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            p[i][i+1]=1
            start=i
            maxlength=2
    length=-1
    for i in range(3,n+1):
        for j in range(n-i+1):
            k=i+j-1
            if s[j]==s[k] and p[j+1][k-1]==1:
                p[j][k]=1
                start=j
                length=i
                if maxlength<length:
                    maxlength=length
                    length=-1
    
    print(maxlength)
    
longest_palindrome('maampreetiiteerp')
                    

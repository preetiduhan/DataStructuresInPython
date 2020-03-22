def decode(s):
    n=len(s)
    res=[]
    i=0
    while(i<n):
        count=1
        ch=s[i]
        while((i+1)<n and s[i]==s[i+1]):
            count+=1
            i+=1
        res.append(ch)
        res.append(str(count))
        i+=1
    print(''.join(res))

decode("wwwwwwaaaabbbccddddd")
        

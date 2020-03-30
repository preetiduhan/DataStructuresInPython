def ugly_numbers(n):
    next_2=2
    next_3=3
    next_5=5
    i=0;j=0;k=0;
    ugly = [0] * n 
    ugly[0]=1
    for ii in range(1,n):
        multiple=min(min(next_5,next_3),next_2)
        ugly[ii]=multiple
        if multiple==next_2:
            i+=1
            next_2=ugly[i]*2
        if multiple==next_3:
            j+=1
            next_3=ugly[j]*3
        if multiple==next_5:
            k+=1
            next_5=ugly[k]*5
    print(ugly)
    print(ugly[-1])

ugly_numbers(150)
    
        
    
    
    

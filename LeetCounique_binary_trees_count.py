def unique_bst(n):
    count=[0 for i in range(n+1)]
    count[0]=1
    count[1]=1
    for i in range(2,n+1):
        for j in range(1,i+1):
            count[i]+=count[i-j]*count[j-1]
    return count[n]
print(unique_bst(3))
print(unique_bst(4))
print(unique_bst(5))
        

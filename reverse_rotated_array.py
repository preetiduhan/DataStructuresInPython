def reverse_util(a):
    l=0
    r=len(a)-1;
    while(l<=r):
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1  
    return a
        
def reverse(a,d):
    if d==0:
        return a
    a1=reverse_util(a[:d+1])
    #print(a1)
    a2=reverse_util(a[d+1:])
    #print(a2)
    a1.extend(a2)
    reverse_util(a1)
    print(a1)

a=[1,2,3,4,5,6]
d=2
reverse(a,d)

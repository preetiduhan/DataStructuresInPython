def ds(num):
    ans=0
    rem=0
    while(num):
        rem=num%10
        ans+=rem
        num=num//10
    return ans

def num_digit_sum(arr):
    hm={}
    maxi=-1
    for i in range(len(arr)):
        digit_sum=ds(arr[i])
        if digit_sum in hm:
            other_val=hm[digit_sum]
            maxi=max(other_val+arr[i],maxi)
            hm[digit_sum]=max(other_val,arr[i])
        else:
            hm[digit_sum]=arr[i]
        print(hm)
    print(maxi)

num_digit_sum([71,17,62,26])
    
        

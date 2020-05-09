'''
longest Peak in an array
'''
def longest_peak(a):
    current_len=0
    longest_peak_len=0
    n=len(a)-1
    i=1
    while i<=n:
        if i+1<=n and a[i]>a[i-1] and a[i]>a[i+1]:
            left_indx=i-2
            while left_indx>=0 and a[left_indx]<a[left_indx+1]:
                left_indx-=1
            right_indx=i+2
            while right_indx<=n and a[right_indx]>a[right_indx+1]:
                right_indx+=1
            current_len=right_indx-left_indx
            longest_peak_len=max(current_len,longest_peak_len)
            i=right_indx
        else:
            i+=1
            continue
    return longest_peak_len
    
a=[2,2,2]
print(longest_peak(a))
        
    

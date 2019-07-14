#---------------insertion sort------------------
def insertion_sort(a):
    for i in range(1,len(a)):
        key = a[i]
        j= i-1
        while(j>=0 and a[j]>key):
            a[j+1] = a[j]
            j=j-1
        a[j+1] = key
    for i in range(0,len(a)):
        print(a[i],end=" ")


insertion_sort([0,5,12,4,12,0])
        
'''Flow goes like this: 
0 5 12 4 12 0                                                                                                                                          
0 5 12 4 12 0                                                                                                                                          
0 4 5 12 12 0                                                                                                                                          
0 4 5 12 12 0                                                                                                                                          
0 0 4 5 12 12  '''

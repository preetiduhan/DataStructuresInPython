'''
[2,1,2,2,2,3,4,2]
[1,3,4,2,2,2,2,2]
'''
def move_elements_to_end(arr,target):
    start=0
    end=len(arr)-1
    print(arr)
    while start<end:
        while(arr[start]!=target):
            start+=1
        while(arr[end]==target):
            end-=1
        if start<end and arr[start]==target and arr[end]!=target:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    print(arr)
        
arr=[2,1,2,2,2,2,3,4,5,2,2,2,6,2,1,3,4,2]
move_elements_to_end(arr,2)
    

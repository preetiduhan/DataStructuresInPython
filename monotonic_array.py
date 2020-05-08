'''
monotonic array
'''
def monotonic_array(arr):
    if len(array)<=2:
        return True
    direction=array[1]-array[0]
    for i in range(2,len(arr)):
        if direction ==0:
            direction=arr[i]-arr[i-1]
            continue
        if breaksdirection(direction,arr[i-1],arr[i]):
            return False
    return True

def breaksDirection(direction,previous,current):
    diff=current-previous
    if direction>0:
        return diff<0
    return diff>0
  
arr=[2,1,2,2,2,2,3,4,5,2,2,2,6,2,1,3,4,2]
monotonic_array(arr,2)
    

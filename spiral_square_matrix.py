'''
spiral on square matrix
'''
def spiral(arr):
    result=[]
    startrow,endrow=0,len(arr)-1
    startcol,endcol=0,len(arr[0])-1
    
    while startrow<=endrow and startcol<=endcol:
        for col in range(startcol,endcol+1):
            result.append(arr[startrow][col])
        for r in range(startrow+1,endrow+1):
            result.append(arr[r][endcol])
        for c in range(endcol-1,startcol-1,-1):
            result.append(arr[endrow][c])
        for r in range(endrow-1,startrow,-1):
            result.append(arr[r][startcol])
        startrow+=1
        endcol=endcol-1
        endrow=endrow-1
        startcol=startcol+1
    print(result)

a = [ [1, 2, 3,4], 
      [7, 8, 9,5], 
      [13, 14, 15,6],
      [7,8,9,10]] 

spiral(a) 
    
    

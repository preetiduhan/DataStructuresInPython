def perm(string,current,index,n):
    if index == n:
        print(current)
        return;
    else:
        perm(string,current+string[index],index+1,n)
        perm(string,current,index+1,n)
        
if __name__ == "__main__": 
    perm('abcd','',0,4)

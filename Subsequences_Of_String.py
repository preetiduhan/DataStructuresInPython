# Print subsequences of string recursively

def subs(string,current,index,n):
    if(index==n):
        output.append(current)
        return
    else:
        subs(string,current+string[index],index+1,n)
        subs(string,current,index+1,n)

output = []
subs('abcd','',0,4)
print(output)

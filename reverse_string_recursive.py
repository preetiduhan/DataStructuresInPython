def reverse_string(sent):
    reverse_string_util_recursive(sent,0)

def reverse_string_util_recursive(sent,index):
    if(index>=len(sent)):
        return 
    else:
        reverse_string_util(sent,index+1)
        print(sent[index],end="")
reverse_string("ilovestorage")

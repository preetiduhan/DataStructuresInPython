'''
Given a string, write a python function to check if it is palindrome or not.

'''
def palindrome(string):
    for i in range(0,int(len(string)/2-1)):
        if(string[i] != string[len(string)-i-1]):
            return False
    return True
    
flag = palindrome('geeg')
print(flag)

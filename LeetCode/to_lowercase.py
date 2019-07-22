'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
'''
class Solution:
    def toLowerCase(self, string: str) -> str:
        r = list(string)
        print(r)
        for i in range(len(string)):
            if r[i]>='A' and r[i]<='Z':
                r[i]=chr(ord(r[i])+32)
        return "".join(r)
                
        

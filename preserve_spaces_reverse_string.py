'''
Write a program to Reverse the given string while preserving the position of spaces.

Examples:

Input  : "abc de"
Output : edc ba

Input : "intern at geeks"
Output : skeegt an retni

Input : "Help others"
Output : sreh topleH
'''
def preserve(sent):
    index_space_list = []
    result =[]
    for i in range(len(sent)):
        if(sent[i] == ' '):
            index_space_list.append(len(sent)-i-1)
    for i in range((len(sent)-1),0,-1):
        if(i in index_space_list):
            result.append(' ')
        if(sent[i]== ' '):
            i=i-1
        result.append(sent[i])
    print(result,end='')

preserve('Help others')      

'''
Given a string str, we need to print reverse of individual words.

Examples:

Input : Hello World
Output : olleH dlroW
 
Input :  Geeks for Geeks
Output : skeeG rof skeeG
'''


def reverse_individual_words(sent):

    start=end=0

    for i in range(len(sent)):

        if(sent[i]==' ' or i == len(sent)-1):

            reverse_string_util(sent,start,end)

            start=end

        end=end+1


def reverse_string_util(sent,start,end):

    if(start>end):

        return

    else:

        reverse_string_util(sent,start+1,end)

        print(sent[start],end="")

reverse_individual_words("i loves storage")

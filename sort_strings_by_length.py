#Sort an array of strings according to string lengths

def strings_sort(l):
    print(sorted(l,key=len))

l = ["GeeksforGeeks", "I", "from", "am"]
strings_sort(l)
print(l)

'''
Learning:

When you pass a lambda to sort, you need to return an integer, not a boolean. So your code should instead read as follows:

xs.sort(lambda x,y: cmp(len(x), len(y)))

Note that cmp is a builtin function such that cmp(x, y) returns -1 if x is less than y, 0 if x is equal to y, and 1 if x is greater than y.

Of course, you can instead use the key parameter:

xs.sort(key = lambda s: len(s))

This tells the sort method to order based on whatever the key function returns.
Simplest way to do this is:

xs.sort(key = len)
 or
print sorted(xs, key=len)
'''


        

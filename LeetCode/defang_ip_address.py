'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
'''
def defangIPaddr(address: str) -> str:
        l = address.split('.')
        print(l)
        r = []
        for i in range(len(l)):
            r.append(l[i])
            r.append('[.]')
        print(''.join(r))
defangIPaddr("1.1.1.1")


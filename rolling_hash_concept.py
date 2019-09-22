```
def hash_function_psa(s,p):
    B = 100000007
    n=len(s)
    psa=[0]*n
    psa[0]=(ord(s[0])-97)*p
    for i in range(1,n):
        psa[i]=(psa[i-1]+(ord(s[i])-97)*pow(p,i+1))%B
    return psa

def hash_function_psb(b,p):
    B = 100000007
    n=len(b)
    psb=[0]*n
    psb[0]=(ord(b[0])-97)*p
    for i in range(1,n):
        psb[i]=(psb[i-1]+(ord(b[i])-97)*pow(p,i+1))%B
    return psb

def check_if_strings_same(a,b,i,j,k,l,p=2):
    B = 100000007
    psa_a=hash_function_psa(a,2)
    psa_b=hash_function_psb(b,2)
    ha=(psa_a[j]-psa_a[i]+(ord(a[i])-97)*pow(p,i+1))%B
    hb=(psa_b[l]-psa_b[k]+(ord(b[k])-97)*pow(p,k+1))%B
    print(ha)
    print(hb)
    d=abs(i-k)
    if i>k:
        hb=hb*pow(p,d)%B
    else:
        ha=ha*pow(p,d)%B
    print(ha)
    print(hb)
    if ha==hb:
        return 1
    else:
        return 0
        

print(check_if_strings_same('preetideepak',"pdeepa",6,10,1,5))
``` 
    

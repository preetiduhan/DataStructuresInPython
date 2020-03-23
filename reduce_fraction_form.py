def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
        
def simple(num1,denm1,num2,denm2):
    
    lcm=gcd(denm1,denm2)
    
    lcm=lcm/(denm1*denm2)
    num3=((lcm/denm1)*num1)+((lcm/denm2)*num2)
    denm3=lcm
    common_factor=gcd(num3,denm3)
    num3=int(num3/common_factor)
    denm3=int(denm3/common_factor)
    print(num3)
    print("/")
    print(denm3)

simple(2,3,6,9)
    
    

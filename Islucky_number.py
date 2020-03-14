def luck_number(n):
    luck_number.counter=2
    if luck_number.counter>n:
        return 1
    if n%luck_number.counter==0:
        return 0
    next_n=n-n/luck_number.counter
    luck_number.counter+=1
    return luck_number(next_n)

print(luck_number(4))

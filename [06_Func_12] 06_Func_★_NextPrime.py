def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(N):
    x=int(N)+1
    while is_prime(x)==False:
        x+=1
    return x
def next_twin_prime(N):
    x=int(N)+1
    a=[]
    while len(a)<2:
        if is_prime(x)==True:
            a.append(x)
            x+=2
            if is_prime(x)==True:
                a.append(x)
            else:
                a=[]
        x+=1
    print('a')
    return a[0],a[1]
exec(input().strip())
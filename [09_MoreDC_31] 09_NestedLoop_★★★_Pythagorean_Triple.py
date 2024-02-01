def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def is_coprime(a,b,c):
    d=[]
    d.append(gcd(a,b))
    d.append(gcd(a,c))
    d.append(gcd(c,b))
    if 1 in d:
        return True
    else:
        return False

def primitive_Pythagorean_triples(max_len):
    a=[]
    for x in range(1,max_len):
        for y in range(x,max_len):
            for z in range(y,max_len):
                if x**2+y**2==z**2:
                    a.append([z,x,y])
    b=[]
    for i in a:
        if is_coprime(i[0],i[1],i[2]):
            b.append(i)
    b.sort()
    c=[]
    for i in b:
        c.append([i[1],i[2],i[0]])
    return c

exec(input().strip())
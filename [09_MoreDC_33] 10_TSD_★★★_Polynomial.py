def add_poly(p1,p2):
    a={i[1]:i[0] for i in p1}
    b={i[1]:i[0] for i in p2}
    for i in b:
        if i in a:
            a[i]+=b[i]
        else:
            a[i]=b[i]
    c=[(i,a[i]) for i in a if a[i]!=0]
    return [(b,a) for a,b in sorted(c)[-1::-1]]

def mult_poly(p1,p2):
    a={i[1]:i[0] for i in p1}
    b={i[1]:i[0] for i in p2}
    c={}
    for i in a:
        for e in b:
            if i+e in c:
                c[i+e]+=a[i]*b[e]
            else:
                c[i+e]=a[i]*b[e]
    d=[(i,c[i]) for i in c if c[i]!=0]
    return [(a,b) for b,a in sorted(d)[-1::-1]]

for i in range(3):
    exec(input().strip())
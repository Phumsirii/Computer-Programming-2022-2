def missing_digits(t):
    a=['0','1','2','3','4','5','6','7','8','9']
    b=[t[n] for n in range(len(t))]
    for c in b:
        if c in a:
            a.remove(c)
    d=[]
    for u in a:
        d.append(int(u))
    return d
exec(input())
def total(pocket):
    a=0
    for i in pocket:
        a+=i*pocket[i]
    return a

def take(pocket, money_in):
    for i in money_in:
        if i in pocket:
            pocket[i]+=money_in[i]
        else:
            pocket[i]=money_in[i]
    return pocket

def pay(pocket,amt):
    a=[]
    for i in pocket:
        a.append(i)
    a.sort()
    b=a[-1::-1]
    y={}
    for c in b:
        if c<=amt:
            d=min(amt//c,pocket[c])
            amt-=(c*d)
            pocket[c]-=d
            y[c]=d
    if amt==0:
        return y
    else:
        for i in y:
            if i in pocket:
                pocket[i]+=y[i]
        return {}
exec(input().strip())
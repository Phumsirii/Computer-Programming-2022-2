def is_odd(n):
    if n%2==1:
        return True
    else:
        return False

def has_odds(x):
    for i in x:
        if is_odd(i):
            return True
    return False

def all_odds(x):
    for i in x:
        if i%2==0:
            return False
    return True

def no_odds(x):
    for i in x:
        if i%2==1:
            return False
    return True

def get_odds(x):
    a=[]
    for i in x:
        if is_odd(i):
            a.append(i)
    return a

def zip_odds(a,b):
    c=get_odds(a)
    d=get_odds(b)
    e=[0]*(len(c)+len(d))
    if len(c)<len(d):
        e[:2*len(c):2]=c
        e[1:2*len(c)+1:2]=d[:len(c):]
        e[2*len(c)::]=d[len(c)::]
    elif len(c)>len(d):
        e[:2*len(d):2]=c[:len(d):]
        e[1:2*len(d):2]=d
        e[2*len(d)::]=c[len(d)::]
    else:
        e[::2]=c
        e[1::2]=d
    return e

exec(input().strip())
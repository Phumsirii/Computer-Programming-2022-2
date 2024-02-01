def make_int_list(x):
    a=x.split()
    b=[]
    for i in a:
        b.append(int(i))
    return b
def is_odd(e):
    if e%2==0:
        return False
    else:
        return True
def odd_list(alist):
    a=[]
    for i in alist:
        if is_odd(i):
            a.append(i)
    return a
def sum_square(alist):
    s=0
    for i in alist:
        s+=i**2
    return s
exec(input().strip())
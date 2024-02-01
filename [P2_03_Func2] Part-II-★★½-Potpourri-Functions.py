def convex_polygon_area(p):
    a=0
    for i in range(len(p)-1):
        a+=(p[i][0]*p[i+1][1])
        a-=(p[i][1]*p[i+1][0])
    a+=p[-1][0]*p[0][1]
    a-=p[-1][1]*p[0][0]
    return abs(a)/2

def is_heterogram(s):
    s=s.lower()
    a=[]
    for i in s:
        if 'a'<=i<='z':
            if i in a:
                return False
            else:
                a.append(i)
    return True

def replace_ignorecase(s,a,b):
    z=0
    while s.lower().find(a.lower(),z)!=-1:
        d=s.lower().find(a.lower(),z)
        c=s[:d:]
        e=s[d+len(a)::]
        s=c+b+e
        z=d+len(b)
    return s

def top3(votes):
    a=[]
    for i in votes:
        a.append([-votes[i],i])
    a.sort()
    b=[]
    for i in range(3):
        b.append(a[i][1])
    return b

for k in range(2):
    exec(input().strip())
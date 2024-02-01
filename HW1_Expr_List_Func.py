def center(r):
    x=float(r[0])
    y=float(r[1])
    w=float(r[2])
    h=float(r[3])
    a=x+w/2
    b=y-h/2
    return [a,b]

def distance(r1,r2):
    c=center(r1)
    d=center(r2)
    e=float(c[0])
    f=float(c[1])
    g=float(d[0])
    h=float(d[1])
    s=((e-g)**2+(f-h)**2)**0.5
    return s

def intersection(r1,r2):
    right1=float(float(r1[0])+float(r1[2]))
    left1=float(r1[0])
    top1=float(r1[1])
    bottom1=float(float(r1[1])-float(r1[3]))
    right2=float(float(r2[0])+float(r2[2]))
    left2=float(r2[0])
    top2=float(r2[1])
    bottom2=float(float(r2[1])-float(r2[3]))
    a=float(min(right1,right2))
    b=float(max(left1,left2))
    w=float(max(a-b,0))
    c=float(min(top1,top2))
    d=float(max(bottom1,bottom2))
    h=float(max(c-d,0))
    return w*h

def union(r1,r2):
    a=abs(float(r1[2])*float(r1[3]))
    b=abs(float(r2[2])*float(r2[3]))
    c=float(intersection(r1,r2))
    return a+b-c

def iou(r1,r2):
    a=intersection(r1,r2)
    b=union(r1,r2)
    return a/b
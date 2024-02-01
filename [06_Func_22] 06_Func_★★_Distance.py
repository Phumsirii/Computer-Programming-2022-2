def distance1(x1, y1, x2, y2):
    dx=abs(float(x1)-float(x2))
    dy=abs(float(y1)-float(y2))
    return (dx**2+dy**2)**0.5
def distance2(p1, p2):
    dx=abs(float(p1[0])-float(p2[0]))
    dy=abs(float(p1[1])-float(p2[1]))
    return (dx**2+dy**2)**0.5
def distance3(c1, c2):
    d=distance2(c1[:2], c2[:2])
    a=c1[2]+c2[2]
    if a>=d:
        c=True
    else:
        c=False
    return d,c
def perimeter(p):
    d=0
    for i in range(len(p)-1):
        d+=distance2(p[i], p[i+1])
    d+=distance2(p[len(p)-1], p[0])
    return d
exec(input().strip())
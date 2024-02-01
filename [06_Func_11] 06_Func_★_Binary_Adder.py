a=[str(e) for e in input().split()]
c=int(a[0],2)+int(a[1],2)
d=bin(c)
print(d[2::])
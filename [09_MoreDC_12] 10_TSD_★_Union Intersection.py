n=int(input())
a=[]
for i in range(n):
    a.append({int(e) for e in input().split()})
u=set()
if len(a)==0:
    i=[]
else:
    i=a[0]
for e in range(len(a)):
    u=u|a[e]
    i=i&a[e]
print(len(u))
print(len(i))
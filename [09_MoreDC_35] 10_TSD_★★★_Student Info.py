n=int(input())
s={}
for i in range(n):
    a=input().split()
    s[a[0]]=[{a[1],a[2],a[3]},[a[1],a[2],a[3]]]
a=set(input().split())
b=[]
for i in s:
    if a<=s[i][0]:
        b.append([i]+s[i][1])
b.sort()
if len(b)==0:
    print('Not Found')
else:
    for i in b:
        print(' '.join(i))
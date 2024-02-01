n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
b=input().split()
for c in b:
    a.append(int(c))
d=int(input())
while d!=(-1):
    a.append(d)
    d=int(input())
e=[a[0]]
for i in range(1,len(a),2):
    e.insert(0,a[i])
for i in range(2,len(a),2):
    e.append(a[i])
print(e)
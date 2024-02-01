a=input()
b=input()
c=0
e=''
for d in b:
    if d in '"(),.' or d in "'":
        e+=' '
    else:
        e+=d
f=e.split()
for g in f:
    if g==a:
        c+=1
print(c)
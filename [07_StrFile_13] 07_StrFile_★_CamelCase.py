a=input()
b=''
c=["'",'"','-','_','.','<','>','/','[',']','(',')','=','+','*',';',':','{','}']
for i in range(len(a)):
    if a[i] in c:
        b+=' '
    else:
        b+=a[i]
if b[0]==' ':
    b=b[1::]
b=b.lower()
d=b[0]
for i in range(1,len(b)):
    if b[i-1]==' ':
        d+=b[i].upper()
    elif b[i]==' ':
        pass
    else:
        d+=b[i]
e=''
for i in range(len(d)):
    if not d[i]==' ':
        e+=d[i]
print(e)
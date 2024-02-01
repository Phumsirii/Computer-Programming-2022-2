d=input()
t=input()
q=True
def count(x,y):
    n=0
    for i in x:
        if i.upper()==y:
            n+=1
    return str(n)
for i in d:
    i=i.upper()
    if not (i=='A' or i=='T' or i=='C' or i=='G'):
        print('Invalid DNA')
        q=False
        break
if t=='R' and q:
    r=''
    for i in d:
        if i.upper()=='A':
            r+='T'
        elif i.upper()=='T':
            r+='A'
        elif i.upper()=='C':
            r+='G'
        elif i.upper()=='G':
            r+='C'
    print(r[-1::-1])
elif t=='F' and q:
    print('A='+count(d,'A')+',','T='+count(d,'T')+',','G='+count(d,'G')+',','C='+count(d,'C'))
elif t=='D' and q:
    w=input().upper()
    n=0
    d=d.upper()
    for i in range(len(d)-1):
        if d[i:i+2:]==w:
            n+=1
    print(n)
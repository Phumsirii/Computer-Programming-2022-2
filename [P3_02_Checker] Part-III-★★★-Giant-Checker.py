def bw(r,c):
    if ord(r)%2==1:
        a=['Black','White']
        return a[int(c)%2]
    else:
        a=['White','Black']
        return a[int(c)%2]

def f(row,column):
    rv=True
    cv=True
    if not 'A'<=row<='z' or len(row)!=1:
        rv=False
    if len(column)==1:
        column='0'+column
    if not '00'<column<='52' or not '0'<=column[0]<='9' or not '0'<=column[1]<='9':
        cv=False
    if rv and cv:
        print(bw(row,column))
    elif rv:
        print('Invalid column')
    elif cv:
        print('Invalid row')
    else:
        print('Invalid row and column')

a=[i.strip() for i in input().split(',')]
if len(a)==1:
    a=a[0]
    r=a[0]
    c=a[1::].strip()
    f(r,c)
else:
    b={}
    for i in a:
        e=i.split('=')
        b[e[0].strip()]=e[1].strip()
    f(b['row'],b['col'])
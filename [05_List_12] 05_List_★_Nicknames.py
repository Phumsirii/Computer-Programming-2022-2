a=['Robert','William','James','John','Margaret','Edward','Sarah','Andrew','Anthony','Deborah']
b=['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']
n=int(input())
d=[]
for i in range(n):
    c=input()
    d.append(c)
for e in d:
    if e in a:
        print(b[a.index(e)])
    elif e in b:
        print(a[b.index(e)])
    else:
        print('Not found')
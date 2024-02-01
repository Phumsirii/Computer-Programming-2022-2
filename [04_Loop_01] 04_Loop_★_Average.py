a=input()
b=0
c=0
while a != 'q':
    b+=float(a)
    c+=1
    a=input()
if c==0:
    print('No Data')
else:
    print(round(b/c,2))
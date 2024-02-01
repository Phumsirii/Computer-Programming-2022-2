a=input().split('/')
b=input().split('-')
c=[int(a[2]),int(a[1]),int(a[0])]
d=[int(b[2]),int(b[1]),int(b[0])]
if c>d:
    print('The second person is older.')
elif d>c:
    print('The first person is older.')
else:
    print('same age')
a=input()
if a[-1]=='s' or a[-1]=='x' or a[-2::1]=='ch':
    a+='es'
elif a[-1]=='y' and not a[-2] in ['a','e','i','o','u']:
    a=a[:-1:]+'i'
    a+='es'
else:
    a+='s'
print(a)
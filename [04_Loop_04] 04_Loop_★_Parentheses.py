a=input()
c=''
for b in a:
    if b=='(':
        c+='['
    elif b=='[':
        c+='('
    elif b==')':
        c+=']'
    elif b==']':
        c+=')'
    else:
        c+=b
print(c)
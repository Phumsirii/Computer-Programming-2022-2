def nolower(x):
    for i in x:
        if x==x.upper():
            return True
    return False
def noupper(x):
    for i in x:
        if x==x.lower():
            return True
    return False
def nono(x):
    a='0123456789'
    for i in x:
        if i in a:
            return False
    return True
def nosym(x):
    a='\'\".,<>?/:;{[}]|\\!@#$%^&*()_-+='
    for i in x:
        if i in a:
            return False
    return True
def rep(s):
    for i in range(len(s)-3):
        if s[i]==s[i+1]==s[i+2]==s[i+3]:
            return True
    return False
def nose(x):
    a='012345678901234567890'
    for i in range(len(x)-3):
        if x[i:i+4] in a or x[i:i+4] in a[-1::-1]:
            return True
    return False
def lese(x):
    a='abcdefghijklmnopqrstuvwxyz'
    for i in range(len(x)-3):
        if x[i:i+4].lower() in a or x[i:i+4].lower() in a[-1::-1]:
            return True
    return False
def kept(x):
    a='!@#$%^&*()_+'
    b='qwertyuiop'
    c='asdfghjkl'
    d='zxcvbnm'
    for i in range(len(x)-3):
        if x[i:i+4].lower() in b or x[i:i+4].lower() in b[-1::-1]\
           or x[i:i+4].lower() in c or x[i:i+4].lower() in c[-1::-1]\
           or x[i:i+4].lower() in d or x[i:i+4].lower() in d[-1::-1]\
           or x[i:i+4] in a or x[i:i+4] in a[-1::-1]:
            return True
    return False
p=input()
e=[]
if len(p)<8:
    e.append("Less than 8 characters")
if nolower(p):
    e.append("No lowercase letters")
if noupper(p):
    e.append("No uppercase letters")
if nono(p):
    e.append("No numbers")
if nosym(p):
    e.append("No symbols")
if rep(p):
    e.append("Character repetition")
if nose(p):
    e.append("Number sequence")
if lese(p):
    e.append("Letter sequence")
if kept(p):
    e.append("Keyboard pattern")
if len(e)==0:
    print('OK')
else:
    for i in e:
        print(i)
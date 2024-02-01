def r(b):
    a={}
    for i in b:
        a[b[i]]=i
    return a

b={'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4','h':'44','i':'444','j':'5','k':'55','l':'555','m':'6','n':'66','o':'666','p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999',' ':'0'}

def text2keys(text):
    c=''
    for i in text.lower():
        if i in b:
            c+=b[i]+' '
    return c.strip()

def keys2text(keys):
    c=''
    d=r(b)
    for i in keys.split():
        if i in d:
            c+=d[i]
    return c
        
exec(input().strip())
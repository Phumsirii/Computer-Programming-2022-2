def knows(r,x,y):
    if y in r[x]:
        return True
    else:
        return False

def is_celeb(r,x):
    if len(r[x])>1:
        return False
    elif len(r[x])==1 and not x in r[x]:
        return False
    for i in r:
        if not x in r[i] and i!=x:
            return False
    return True

def find_celeb(r):
    for i in r:
        if is_celeb(r,i):
            return i
        
def read_relations():
    a=input().strip().split()
    b={}
    while a[0]!='q':
        if not a[0] in b:
            b[a[0]]=set()
        if not a[1] in b:
            b[a[1]]=set()
        b[a[0]].add(a[1])
        a=input().strip().split()
    return b

def main():
    r=read_relations()
    c=find_celeb(r)
    if c==None:
        print('Not Found')
    else:
        print(c)

exec(input().strip())
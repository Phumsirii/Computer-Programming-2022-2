def index_of(grades, ID):
    a=False
    for b in grades:
        if b[0]==ID:
            a=True
            c=grades.index(b)
    if a:
        return c
    else:
        return -1
def upgrade(grades, IDs):
    a=['F','D','D+','C','C+','B','B+','A','A']
    for b in grades:
        if b[0] in IDs:
            b[1]=a[a.index(b[1])+1]
    grades.sort()
exec(input())
exec(input())
exec(input())
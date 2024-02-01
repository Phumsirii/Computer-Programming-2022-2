a=input()
b=input()
score=0
n=0
if len(a)==len(b):
    while n<len(a):
        if b[n]==a[n]:
            score+=1
        n+=1
    print(score)
else:
    print('Incomplete answer')
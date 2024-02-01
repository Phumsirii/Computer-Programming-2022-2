a=input().split()
b=[int(i) for i in a]
n=0
for c in range(1,len(b)-1):
    if b[c]>b[c-1] and b[c]>b[c+1]:
        n+=1
print(n)
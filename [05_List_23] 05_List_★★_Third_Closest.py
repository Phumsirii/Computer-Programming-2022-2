a=int(input())
b=[]
for i in range(a):
    c=input().split()
    b.append([(float(c[0])**2+(float(c[1])**2))**0.5,i+1,c[0],c[1]])
b.sort()
print('#'+str(b[2][1])+':','('+str(float(b[2][2]))+',',str(float(b[2][3]))+')')
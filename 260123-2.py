#x = list('1234567890')
#x[1::2]=['0']*len(x[1::2])
#print(x)

s = '1234abcd'
a=s[:int(len(s)/2):]
b=s[int(len(s)/2)::]
print(a)
print(b)

#s = 'abcde'
#a=s[:len(s)-1:]+'*'
#print(a)
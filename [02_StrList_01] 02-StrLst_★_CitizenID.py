a=list(input())
b=(11-(13*int(a[0])+12*int(a[1])+11*int(a[2])+10*int(a[3])+9*int(a[4])+8*int(a[5])+7*int(a[6])+6*int(a[7])+5*int(a[8])+4*int(a[9])+3*int(a[10])+2*int(a[11]))%11)%10
print(a[0],a[1]+a[2]+a[3]+a[4],a[5]+a[6]+a[7]+a[8]+a[9],a[10]+a[11],str(b))
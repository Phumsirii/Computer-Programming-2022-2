a=['','et','song','sam','si','ha','hok','chet','paet','kao']
y=['','et','song','sam','si','ha','hok','chet','paet','kao']
b=['','sip ','yi sip ','sam sip ','si sip ','ha sip ','hok sip ','chet sip ','paet sip ','kao sip ']
c=['','neung','song','sam','si','ha','hok','chet','paet','kao']
w=['','neung roi ','song roi ','sam roi ','si roi ','ha roi ','hok roi ','chet roi ','paet roi ','kao roi ']
x=['','neung pun ','song pun ','sam pun ','si pun ','ha pun ','hok pun ','chet pun ','paet pun ','kao pun ']
z=['soon','neung','song','sam','si','ha','hok','chet','paet','kao','sip']
def to_Thai(n):
    d=n%10
    e=n%100//10
    f=n//100%10
    g=n//1000
    if n<=10:
        return z[n]
    if 11<=n<=99:
        return b[e]+y[d]
    if 100<=n<=999:
        return w[f]+b[e]+y[d]
    if 1000<=n<=9999:
        return x[g]+w[f]+b[e]+a[d]
exec(input().strip())
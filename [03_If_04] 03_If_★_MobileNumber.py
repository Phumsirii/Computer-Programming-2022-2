a=str(input())
b=a[:2:]
if len(a)==10:
    if b=='06' or b=='08' or b=='09' :
        print('Mobile number')
    else:
        print('Not a mobile number')
else:
    print('Not a mobile number')
a=int(input())
if a<=100:
    print(18)
else:
    if 100<a<=250:
        print(22)
    else:
        if 250<a<=500:
            print(28)
        else:
            if 500<a<=1000:
                print(38)
            else:
                if 1000<a<=2000:
                    print(58)
                else:
                    print('Reject')
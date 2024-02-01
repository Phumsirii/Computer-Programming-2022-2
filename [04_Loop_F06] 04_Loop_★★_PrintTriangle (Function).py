def print_triangle(h):
    h=int(h)
    print('.'*(h-1)+'*')
    for i in range(1,h-1):
        print('.'*(h-i-1)+'*'+'.'*(2*i-1)+'*')
    print('*'*(2*h-1))
exec(input())
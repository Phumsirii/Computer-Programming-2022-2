def mosteller(w, h):
    a=((w*h)**(0.5))/60
    return a
def du_bois(w, h):
    b=0.007184*(w**0.425)*(h**0.725)
    return b
def fujimoto(w, h):
    c=0.008883*(w**0.444)*(h**0.663)
    return c
def main():
    w=float(input())
    h=float(input())
    a=((w*h)**(0.5))/60
    b=0.007184*(w**0.425)*(h**0.725)
    c=0.008883*(w**0.444)*(h**0.663)
    print("Mosteller =", round(a, 5))
    print("Du Bois =", round(b, 5))
    print("Fujimoto =", round(c,5))
exec(input()) 
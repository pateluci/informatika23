a=int(input("vložte a"))
b=int(input("vložte b"))
c=int(input("vložte c"))

def solve_quadratic_equasion(a, b, c):
    D=b**2 - 4*a*c

    if a==0 and b==0 and c==0:
        print("Rovnice má nekonečně mnoho řešení")
    elif a==0 and b==0:
        print("Rovnice nemá řešení")
    elif a==0:
        print(-c/b)
    else:
        x1=(-b+D**0.5) /2*a
    x2=(-b-D**0.5) /2*a
    print(x1, x2)   






solve_quadratic_equasion(a, b, c)

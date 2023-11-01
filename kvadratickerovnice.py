a=int(input("vložte a"))
b=int(input("vložte b"))
c=int(input("vložte c"))

def solve_quadratic_equasion(a, b, c):
    D=b**2 - 4*a*c

    x1=(-b+D**0.5) /2*a
    x2=(-b-D**0.5) /2*a
    print(x1, x2)   




solve_quadratic_equasion(a, b, c)
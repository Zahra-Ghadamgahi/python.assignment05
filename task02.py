import math
def solve_quadratic_equation(a, b, c):
    function = b**2 - 4*a*c
    if function > 0:
        root_1 = (-b + math.sqrt(function)) / (2*a)
        root_2 = (-b - math.sqrt(function)) / (2*a)
        return root_1, root_2
    elif function == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots exist"

a = float(1)
b = float(-3)
c = float(2)
roots = solve_quadratic_equation(a, b, c)
print(roots)

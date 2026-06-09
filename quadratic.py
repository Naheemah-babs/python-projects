import math

def quadratic(a, b, c):
    determinant = (b ** 2) - (4 * a * c)

    if determinant < 0:
        return "the equation has no roots"
    elif determinant == 0:
        x = -b / (2 * a)
        return f"the equation has only one root which is {x}"
    else:
        x1 = (-b + math.sqrt(determinant)) / (2 * a)
        x2 = (-b - math.sqrt(determinant)) / (2 * a)
        return f"The two roots are: {x1} and {x2}"

print(quadratic(1, -3, 2))
print(quadratic(1, 1, 5))
print(quadratic(1, -4, 4))
print(quadratic(1, -5, 6))
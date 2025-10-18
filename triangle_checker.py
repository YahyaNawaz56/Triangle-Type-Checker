# triangle_checker.py
# Program to determine the type of triangle

def check_triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"

    # Check for Isosceles or Scalene
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check for angles (Acute, Right, Obtuse)
    sides = sorted([a, b, c])
    x, y, z = sides
    if z**2 == x**2 + y**2:
        angle_type = "Right"
    elif z**2 < x**2 + y**2:
        angle_type = "Acute"
    else:
        angle_type = "Obtuse"

    return f"{angle_type} {triangle_type} triangle"


# Example executions
if __name__ == "__main__":
    a = int(input("Enter side 1: "))
    b = int(input("Enter side 2: "))
    c = int(input("Enter side 3: "))
    print(check_triangle_type(a, b, c))

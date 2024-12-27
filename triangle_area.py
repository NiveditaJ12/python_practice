# Find area of triangle

def area_of_triangle(b,h):
    area = 0.5*b*h
    return area

base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the trianle: '))
print(f'The area of triangle is {area_of_triangle(base, height)}')
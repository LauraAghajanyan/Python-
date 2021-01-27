

def segment_length(x1, y1, x2, y2, x3, y3, x4, y4):

    a = ((x2 - x1) * (x2 - x1) - (y2 - y1) * (y2 - y1))**0.5
    b = ((x3 - x2) * (x3 - x2) - (y3 - y2) * (y3 - y2))**0.5
    c = ((x4 - x3) * (x4 - x3) - (y4 - y3) * (y4 - y3))**0.5
    d = ((x4 - x1) * (x4 - x1) - (y4 - y1) * (y4 - y1))**0.5

    perimeter = a+b+c+d
    return perimeter


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))
x4 = float(input("Enter x4: "))
y4 = float(input("Enter y4: "))

print(segment_length(x1, y1, x2, y2, x3, y3, x4, y4))


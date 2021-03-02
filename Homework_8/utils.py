import sys

def generator(start, stop):
    for i in range(start, stop):
        number = True
        current = i
        while i > 0:
            if (i % 10) % 2 == 0:
                number = False
            i /= 10
        if number:
           yield current

print(sys.argv)
if len(sys.argv) == 1:
    start = int(input("Enter the start: "))
    stop = int(input("Ener the stop: "))
if len(sys.argv) == 3:
    start = int(sys.argv[1])
    stop = int(sys.argv[2])
    if start >= stop:
        print("Invalid input! ")
    else:
        for i in generator(start, stop):
            print(i)
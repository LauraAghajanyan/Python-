number = input("Enter a number: ")
l = len(number)
suml = 0
sumr = 0
if l % 2 == 0:
    for i in range(l//2):
        suml += int(number[i])
    for j in range(l//2, l):
        sumr += int(number[j])
if suml == sumr:
    print("Yes")
else:
    print("No")

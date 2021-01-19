num = input("Enter a number: ")
sum = 0
for i in num:
    sum += int(i)

def count(sum):
    result = 0
    sum = str(sum)
    for i in sum:
        result += int(i)
    return result

while count(sum) > 9:
    count(sum)


print(count(sum))



numbers = input("Enter numbers: ").split()
list = []  # create a list where the products will be added
for i in range(len(numbers)-1):
    a = int(numbers[i])
    b = int(numbers[i+1])
    list.append(a * b)  # adds the products
print(max(list))  # prints the largest product

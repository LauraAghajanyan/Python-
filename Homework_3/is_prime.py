
def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    for i in range(2,num//2):
        if num % i == 0:
            return False
        else:
            return True


num = int(input("Enter a number: "))
if is_prime(num):
    print("Yes")
else:
    print("No")

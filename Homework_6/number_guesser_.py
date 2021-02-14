import random
p = input("Input 0 to start! ")


def number_guesser(low, high):
    low = 1
    high = 1000
    count = 0
    while count < 10 and x != 0:
        num = random.randint(low, high)
        x = int(input("My guess number " + str(count) + str(num)))
        if x == 1:
            low = (low + high)//2
            count += 1
            return number_guesser(low, high)
        if x == -1:
            high = (low+high)//2
            count += 1
            return number_guesser(low, high)

        if count == 10:
            print("I couldn’t guess in 10 steps! This means you cheated! ")
            break
    print(" I guessed in 10 steps! ")

if p == 0:
    print(number_guesser(1, 1000))



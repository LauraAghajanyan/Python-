
p = int(input("Input 0 to start: "))


def number_guesser(low, high):
    bool_num = False
    count = 0
    while count < 10:
        num = (low + high) // 2
        x = int(input("My guess number " + str(num)))
        if x == 1:
            low = num
            count += 1
            return number_guesser(low, high)
        if x == -1:
            high = num
            count += 1
            return number_guesser(low, high)
        if x == 0:
            bool_num = True
            print("I guessed your number")
            break
    if bool_num == False:
        print("You cheated! ")


if p == 0:
    number_guesser(1, 1000)



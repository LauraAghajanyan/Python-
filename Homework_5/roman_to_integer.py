def roman_to_integer(num):
    rom_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # XII = 10+1+1
    # IX = 10 - 1 = 9

    integer = 0
    for i in range(0, len(num)-1):
        if rom_int[num[i]] >= rom_int[num[i+1]]:
            integer += rom_int[num[i]]
        if rom_int[num[i]] <= rom_int[num[i+1]]:
            integer += rom_int[num[i+1]] - rom_int[num[i]]
    return integer


num = input("Enter a roman number: ")
print(roman_to_integer(num))


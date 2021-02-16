import random

def get_a_random_word():
    with open("fruits.txt") as f:
        fruits = [row for row in f.readlines()]
        return random.choice(fruits)


word = get_a_random_word()
wrongs = len(word) - 1
letters = "-" * len(word)
wrong = 0
while wrong < wrongs and letters != word:
    print("Guess the word: ", letters)
    guess = input("Guess a letter: ").upper()
    print()
    if guess in word:
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += letters[i]
        letters = new
    else:
        print(len(word) - wrong, "mistakes left")
        wrong += 1
if wrong == wrongs:
    print("You lost the game! ")
else:
    print("You won the game! ")



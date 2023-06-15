import random


def guess(x):
    guess_num = random.randint(1, x)
    number = 0
    for i in range(1, 4):
        number = int(input(f"guess the number between 1 and {x}: "))
        if number > x or number < 1:
            number = int(input(f"please choose the number between 1 and {x}: "))
        if number < guess_num:
            print(f"sorry, {number} is low")
        elif number > guess_num:
            print(f"sorry, {number} is high")
    if number != guess_num:
        print("your chance is finished, try again.")
        print(f"correct answer is {guess_num}")
    else:
        print(f"you have guessed correct number {guess_num} ")


guess(20)

import random

print("""\
Guess a random integer between 1 and 1000
""")

answer = random.randint(0,1000)
for n in range(0, 10):
    guess = int(input("Guess: "))
    if guess < answer:
        print("low!!")
    elif guess == answer:
        print("correct, it is", answer)
        break
    else:
        print("high!!")

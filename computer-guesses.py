import random

print("""\
Pick a random integer between 1 and 1000
When I give you a guess tell if it is:
    l for low
    h for high
    k for kudos    
""")
start, end = 0, 1000
answer = random.randint(start,end)
for n in range(0, 14):
    guess = input("Is it "+str(answer)+"?")
    if guess == "l":
        start = answer+1
        answer = random.randint(start,end)
    elif guess == "k":
        print("Hurray!!")
        break
    elif guess == "h":
        end = answer-1
        answer = random.randint(start,end)
    else:
        print("Enter only l, h or k")
    




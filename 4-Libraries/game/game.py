import random

while True:
    prompt = int(input("Guess: "))
    if prompt < 0:
        continue
    else:
        break

mys_number = random.randint(1, 100)

while True:

    prompt = int(input("What's the level: "))

    if prompt < 0:
        continue
    elif prompt < mys_number:
        print("Too small!")
        continue
    elif prompt > mys_number:
        print("Too big")
    elif prompt == mys_number:
        print("Just right")
        break
    else:
        print("error")

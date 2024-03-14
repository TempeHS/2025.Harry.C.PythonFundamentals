import random

correct = 0
incorrect = 0
attempts = 0

while True:
    for i in range(10):
        x = random.randint(1, 9)
        y = random.randint(1, 9)

        answer = x + y

        for i in range(3):
            prompt = int(input(f"What's the answer to {x} + {y}: "))
            if prompt == answer:
                correct += 1
                break
            elif prompt != answer:
                attempts += 1
                incorrect += 1
                print("EEE")
        print(f"{x} + {y} = {answer}")

    break

total = 10 - incorrect
print(f"You got : {total}/10")

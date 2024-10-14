import random


names = []
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)


random_name = random.choice(names)

print(f"The randomly chosen name is: {random_name}")

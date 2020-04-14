import random

name = input("Enter your name: ")
print(f'Hello, {name}')

_set = input()
if not _set:
    options = ['rock', 'paper', 'scissors']
else:
    options = _set.split(',')

combos = {}

increment = int((len(options) - 1) / 2)

for option in options:
    if options.index(option) + increment > len(options) - 1:
        variance = int((options.index(option) + increment) -
                       (len(options) - 1))
        items = tuple(options[options.index(
            option) + 1::] + options[0:variance])
        combos[option] = items
    else:
        items = tuple(options[options.index(
            option) + 1:options.index(option) + increment + 1])
        combos[option] = items

rating_file = open('rating.txt', 'r+')
scores = {}
writing_list = ""

for score in rating_file:
    username, rating = score.split()
    scores[username] = int(rating)


if name not in scores:
    scores[name] = 0

rating_file.close()

print("Okay, let's go")

while True:
    user_choice = input()
    comp_choice = random.choice(options)
    if user_choice == "!exit":
        print("Bye!")
        break
    elif user_choice == "!rating":
        print(f'Your rating: {scores[name]}')
        continue
    try:
        if user_choice == comp_choice:
            print(f"There is a draw ({user_choice})")
            scores[name] += 50
        elif user_choice in combos[comp_choice]:
            print(f"Well done. Computer chose {comp_choice} and failed")
            scores[name] += 100
        elif comp_choice in combos[user_choice]:
            print(f"Sorry, but computer chose {comp_choice}")
    except KeyError:
        print("Invalid input")

items = scores.items()
for item in items:
    writing_list += f'{item[0]} {item[1]}\n'

finished_file = open('rating.txt', 'w')

finished_file.write(writing_list)

finished_file.close()

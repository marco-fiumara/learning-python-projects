water = 400
milk = 540
beans = 120
cups = 9
money = 550


def print_state(w, m, b, c, mon):
    print(f"""{w} of water
{m} of milk
{b} of coffee beans
{c} of disposable cups
${mon} of money""")


def buy():
    espresso = [-250, 0, -16, -1, 4]
    latte = [-350, -75, -20, -1, 7]
    cappucino = [-200, -100, -12, -1, 6]
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    option = input()
    if option == "1":
        return espresso
    elif option == "2":
        return latte
    elif option == "3":
        return cappucino
    elif option == "back":
        return "back"
    else:
        return "Error"


def resource_check(w, m, b, c):
    if water + w < 0:
        return "Sorry, not enough water!"
    elif milk + m < 0:
        return "Sorry, not enough milk!"
    elif beans + b < 0:
        return "Sorry, not enough coffee beans!"
    elif beans + c < 0:
        return "Sorry, not enough disposable cups!"
    else:
        return "Good"


def fill():
    options = []
    print("Write how many ml of water do you want to add:")
    options.append(int(input()))
    print("Write how many ml of milk do you want to add:")
    options.append(int(input()))
    print("Write how many grams of coffee beans do you want to add:")
    options.append(int(input()))
    print("Write how many disposable cups of coffee do you want to add:")
    options.append(int(input()))
    return options


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    choice = input()
    print()
    if choice == "buy":
        result = buy()
        if result == "back":
            print()
            continue
        check_result = resource_check(
            result[0], result[1], result[2], result[3])
        if check_result == "Good":
            water += result[0]
            milk += result[1]
            beans += result[2]
            cups += result[3]
            money += result[4]
            print("I have enough resources, making you a coffee!")
            print()
        else:
            print(check_result)
            print()
    elif choice == "fill":
        result = fill()
        water += result[0]
        milk += result[1]
        beans += result[2]
        cups += result[3]
        print()
    elif choice == "take":
        print(f"I gave you {money}")
        money = 0
        print()
    elif choice == "remaining":
        print_state(water, milk, beans, cups, money)
        print()
    elif choice == "exit":
        break
    else:
        print("Error")

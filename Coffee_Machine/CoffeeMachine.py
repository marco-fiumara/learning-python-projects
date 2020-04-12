class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    espresso = [-250, 0, -16, -1, 4]
    latte = [-350, -75, -20, -1, 7]
    cappuccino = [-200, -100, -12, -1, 6]

    user_input = None
    state = "default"

    def setState(self):
        self.state = "default"
        self.user_input = None
        print()

    def buy(self, entry):
        if entry == "1":
            return self.espresso
        elif entry == "2":
            return self.latte
        elif entry == "3":
            return self.cappuccino
        elif entry == "back":
            return "back"
        else:
            return "Error"

    def resourceCheck(self, w, m, b, c):
        if self.water + w < 0:
            return "Sorry, not enough water!"
        elif self.milk + m < 0:
            return "Sorry, not enough milk!"
        elif self.beans + b < 0:
            return "Sorry, not enough coffee beans!"
        elif self.cups + c < 0:
            return "Sorry, not enough disposable cups!"
        else:
            return "Good"

    def fill(self):
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

    def choice(self):
        while True:
            # Default selection option
            if self.state == "default":
                print("Write action (buy, fill, take, remaining, exit):")
                self.user_input = input()
                if self.user_input == "buy" or "fill" or "take" or "remaining" or "exit":
                    self.state = self.user_input
                    print()
                else:
                    self.setState()
                    continue
            # Buy selection option
            if self.state == "buy":
                print(
                    "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                option = input()
                result = self.buy(option)
                if result == "back":
                    self.setState()
                    self.choice()
                    continue
                check_result = self.resourceCheck(
                    result[0], result[1], result[2], result[3])
                if check_result == "Good":
                    self.water += result[0]
                    self.milk += result[1]
                    self.beans += result[2]
                    self.cups += result[3]
                    self.money += result[4]
                    print("I have enough resources, making you a coffee!")
                    self.setState()
                    continue
                else:
                    print(check_result)
                    self.setState()
                    continue
            # Fill selection option
            elif self.state == "fill":
                result = self.fill()
                self.water += result[0]
                self.milk += result[1]
                self.beans += result[2]
                self.cups += result[3]
                self.setState()
                continue
            # Take selection option
            elif self.state == "take":
                print(f"I gave you ${self.money}")
                self.money = 0
                self.setState()
                continue
            # Remaining selection option
            elif self.state == "remaining":
                print(
                    f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.beans} of coffee beans\n{self.cups} of disposable cups\n${self.money} of money")
                self.state = "default"
                self.user_input = None
                print()
                continue
            elif self.state == "exit":
                break

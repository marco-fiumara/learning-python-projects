class CoffeeMachine:
    menu = {
        '1': [250, 0, 16, 4],
        '2': [350, 75, 20, 7],
        '3': [200, 100, 12, 6],
    }

    def __init__(self, water=0, milk=0, coffee=0, cups=0, money=0):
        self.active = True
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def action(self):
        try:
            action = getattr(self, input(
                'Write action (buy, fill, take, remaining, exit): '))
            print()
            action()
        except AttributeError:
            print('Unknown action')

    def buy(self):
        choices = '1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu'
        choice = input(f'What do you want to buy? {choices}: ')
        if choice not in ['1', '2', '3', 'back']:
            print('Unknown variety of coffee')
            return

        if choice == 'back':
            return

        missing_resources = self.__calculate_missing_resources(
            *CoffeeMachine.menu[choice][:-1])
        if len(missing_resources) > 0:
            print('Sorry, not enough %s!' % ''.join(missing_resources))
            return

        print('I have enough resources, making you a coffee!')

        self.__recalculate_resources(*CoffeeMachine.menu[choice])

    def __calculate_missing_resources(self, water, milk, coffee):
        missing_resources = []

        if self.water < water:
            missing_resources.append('water')
        if self.milk < milk:
            missing_resources.append('milk')
        if self.coffee < coffee:
            missing_resources.append('coffee beans')
        if self.cups == 0:
            missing_resources.append('disposable cups')

        return missing_resources

    def __recalculate_resources(self, water, milk, coffee, money):
        self.water -= water
        self.milk -= milk
        self.coffee -= coffee
        self.cups -= 1
        self.money += money

    def fill(self):
        self.water += int(input('Write how many ml of water the coffee machine has: '))
        self.milk += int(input('Write how many ml of milk the coffee machine has: '))
        self.coffee += int(input('Write how many grams of coffee beans the coffee machine has: '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: '))

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def remaining(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def exit(self):
        self.active = False


machine = CoffeeMachine(400, 540, 120, 9, 550)

while machine.active:
    machine.action()
    print()

import random


class TicTacToe:
    cell_dict = {
        (1, 3): [0, 0], (2, 3): [0, 1], (3, 3): [0, 2],
        (1, 2): [1, 0], (2, 2): [1, 1], (3, 2): [1, 2],
        (1, 1): [2, 0], (2, 1): [2, 1], (3, 1): [2, 2],
    }

    def __init__(self, active):
        self.avaliable_dict = {(0, 0): (1, 3), (0, 1): (2, 3), (0, 2): (3, 3), (
            1, 0): (1, 2), (1, 1): (2, 2), (1, 2): (3, 2), (2, 0): (1, 1), (2, 1): (2, 1), (2, 2): (3, 1)}
        self.active = active
        self.cells = list(" " * 9)
        self.choice()
        self.choice_x = self.choices[1] if len(self.choices) > 1 else None
        self.choice_y = self.choices[2] if len(self.choices) > 1 else None
        self.turn = self.choice_x
        self.x = 0
        self.o = 0
        self.character = 0
        self.reshape()
        self.output()

    def choice(self):
        self.choices = input('Input command: ')
        self.choices = self.choices.split()
        self.command = self.choices[0]
        if self.command != 'exit' and self.command != 'start':
            self.choice()
        elif self.command == 'exit':
            self.exit_func()
            exit()

    def reshape(self):
        cells = []
        for i in range(0, 9, 3):
            cells.append(self.cells[i:i+3])
        self.cells = cells

    def output(self):
        print("-" * 9)
        for element in self.cells:
            print("| " + " ".join(letter for letter in element) + " |")
        print("-" * 9)

    def input(self):
        if self.turn == "user":
            try:
                coord_a, coord_b = (int(x) for x in input(
                    "Enter the coordinates: ").split(" "))
                coord_a, coord_b = TicTacToe.cell_dict[coord_a, coord_b]
            except ValueError:
                print("You should enter numbers!")
            except EOFError:
                print("You should enter numbers!")
            except KeyError:
                print("Coordinates should be from 1 to 3!")
            else:
                if self.cells[coord_a][coord_b] != " ":
                    print("This cell is occupied! Choose another one!")
                    return None
                self.playerMove(coord_a, coord_b)
        else:
            self.compMove()

    def playerMove(self, coord_a, coord_b):

        self.cells[coord_a][coord_b] = "X" if self.character % 2 == 0 else "O"
        del self.avaliable_dict[(coord_a, coord_b)]
        self.turn = self.choice_y if self.character % 2 == 0 else self.choice_x
        self.character += 1
        self.output()
        self.status()

    def compMove(self):
        print('Making move level "easy"')
        move = random.choice(list(self.avaliable_dict.items()))
        coords = TicTacToe.cell_dict[move[1]]
        self.cells[coords[0]][coords[1]
                              ] = "X" if self.character % 2 == 0 else "O"
        del self.avaliable_dict[move[0]]
        self.turn = self.choice_y if self.character % 2 == 0 else self.choice_x
        self.character += 1
        self.output()
        self.status()

    def status(self):
        if any([all([x == "X" for x in self.cells[i]]) for i in range(3)]) \
                or any([all([x == "X" for i in range(3) for x in self.cells[i][j]])for j in range(3)]) \
                or all(x == "X" for i in range(3) for x in self.cells[i][i]) \
                or all(x == "X" for i in range(3) for x in self.cells[i][2-i]):
            print("X wins")
            print()
            self.loop()
        elif any([all([x == "O" for x in self.cells[i]]) for i in range(3)]) \
                or any([all([x == "O" for i in range(3) for x in self.cells[i][j]])for j in range(3)]) \
                or all(x == "O" for i in range(3) for x in self.cells[i][i]) \
                or all(x == "O" for i in range(3) for x in self.cells[i][2-i]):
            print("O wins")
            print()
            self.loop()
        elif any(" " in element for i in range(3) for element in self.cells[i]):
            return None
        else:
            print("Draw")
            print()
            self.loop()

    def exit_func(self):
        self.active = False

    def loop(self):
        self.__init__(True)


# start of the game
Game = TicTacToe(True)

while Game.active:
    Game.input()

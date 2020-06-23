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
        if self.turn == 'easy':
            print('Making move level "easy"')
            self.compAction(self.compMoveEasy())
        elif self.turn == 'medium':
            print('Making move level "medium"')
            self.compAction(self.compMoveMedium())
        elif self.turn == 'hard':
            self.compMoveHard(0)

    def compMoveEasy(self):
        move = random.choice(list(self.avaliable_dict.items()))
        return TicTacToe.cell_dict[move[1]]

    def compMoveMedium(self):
        # Row check
        row_number = -1
        for row in self.cells:
            row_number += 1
            if row.count(" ") == 1 and (row.count('X') == 2 or row.count('O') == 2):
                return [row_number, row.index(" ")]

        # Column check
        columns = [[(0, 0), (1, 0), (2, 0)], [
            (0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
        for possibility in columns:
            empty_count = 0
            x_count = 0
            o_count = 0
            empty_index = None
            for coordinate in possibility:
                if self.cells[coordinate[0]][coordinate[1]] == 'X':
                    x_count += 1
                elif self.cells[coordinate[0]][coordinate[1]] == 'O':
                    o_count += 1
                elif self.cells[coordinate[0]][coordinate[1]] == " ":
                    empty_count += 1
                    empty_index = [coordinate[0], coordinate[1]]
                if (x_count == 2 or o_count == 2) and empty_count == 1:
                    return empty_index

        # Diagonal check
        diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
        for possibility in diagonals:
            empty_count = 0
            x_count = 0
            o_count = 0
            empty_index = None
            for coordinate in possibility:
                if self.cells[coordinate[0]][coordinate[1]] == 'X':
                    x_count += 1
                elif self.cells[coordinate[0]][coordinate[1]] == 'O':
                    o_count += 1
                elif self.cells[coordinate[0]][coordinate[1]] == " ":
                    empty_count += 1
                    empty_index = [coordinate[0], coordinate[1]]
                if (x_count == 2 or o_count == 2) and empty_count == 1:
                    return empty_index

        return (self.compMoveEasy())

    def compMoveHard(self, depth):
        moves = list(self.avaliable_dict)
        if len(moves) == 1:
            return moves[0]
        else:
            self.cells[(moves[depth][0])(moves[depth][1])
                       ] = "X" if self.character % 2 == 0 else "O"
            if self.status() == ("X Wins" or "O Wins"):
                del self.cells[(moves[depth][0])(moves[depth][1])]
                self.compAction(moves[depth])
            elif self.status() == ("Draw"):
                del self.cells[(moves[depth][0])(moves[depth][1])]
                self.compAction(moves[depth])
            else:
                self.compMoveHard(depth + 1)

    def compAction(self, coordinates):
        self.cells[coordinates[0]][coordinates[1]
                                   ] = "X" if self.character % 2 == 0 else "O"
        del self.avaliable_dict[(coordinates[0], coordinates[1])]
        self.turn = self.choice_y if self.character % 2 == 0 else self.choice_x
        self.character += 1
        self.output()
        result = self.status()
        if result == "X Wins":
            print("X wins")
            print()
            self.loop()
        elif result == "O Wins":
            print("O Wins")
            print()
            self.loop()
        elif result == "Draw":
            print("Draw")
            print()
            self.loop()

    def status(self):
        if any([all([x == "X" for x in self.cells[i]]) for i in range(3)]) \
                or any([all([x == "X" for i in range(3) for x in self.cells[i][j]])for j in range(3)]) \
                or all(x == "X" for i in range(3) for x in self.cells[i][i]) \
                or all(x == "X" for i in range(3) for x in self.cells[i][2-i]):
            return "X Wins"
        elif any([all([x == "O" for x in self.cells[i]]) for i in range(3)]) \
                or any([all([x == "O" for i in range(3) for x in self.cells[i][j]])for j in range(3)]) \
                or all(x == "O" for i in range(3) for x in self.cells[i][i]) \
                or all(x == "O" for i in range(3) for x in self.cells[i][2-i]):
            return "O Wins"
        elif any(" " in element for i in range(3) for element in self.cells[i]):
            return None
        else:
            return "Draw"

    def exit_func(self):
        self.active = False

    def loop(self):
        self.__init__(True)


# start of the game
Game = TicTacToe(True)

while Game.active:
    Game.input()
